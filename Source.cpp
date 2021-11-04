#define _CRT_SECURE_NO_WARNINGS
#include <filesystem>
#include <sstream>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <ranges>
#include <optional>

using namespace std::literals::string_literals;
namespace fs = std::filesystem;

std::optional<std::string> homeDir() {
	auto homeDir{ ""s };
	for (auto elem : { "HOMEDRIVE", "HOMEPATH" }){
		if (auto path = std::getenv(elem); path != nullptr)
			homeDir += std::string{ path };
		else
			return {};
	}
	return homeDir;
}

void searchDrive(fs::path folder)
{
	auto songsOutput = std::fstream{ R"(..\details\songfile.txt)", std::ios_base::out };
	auto songsPathOutput = std::fstream{ R"(..\details\songpath.txt)", std::ios_base::out };
	std::ostringstream output;
	std::ostringstream output2;
	auto isFile = [](const fs::path file) {return file.filename().extension() == ".mp3"; };
	std::list<std::string> pathVec, fileNamevec;
	try {
		for (auto const& entry : fs::recursive_directory_iterator(folder, fs::directory_options::skip_permission_denied)) {
			try {
				if (isFile(entry)) {
					fileNamevec.emplace_back(entry.path().filename().string() + "\n");
					pathVec.emplace_back(entry.path().parent_path().string() + "\n");
				}
			}
			catch (fs::filesystem_error const&) {}
			catch (std::exception const& ) {}
		}
		
		std::ranges::copy(fileNamevec, std::ostream_iterator<std::string>(output));
		songsOutput << output.str();
		std::ranges::copy(pathVec, std::ostream_iterator<std::string>(output2));
		songsPathOutput << output2.str();
		songsOutput.close();
		songsPathOutput.close();

	}
	catch (fs::filesystem_error const&) {}
	catch (std::exception const&) {}
}
int main() {
	fs::path folder{ std::format(R"({}\Music)", homeDir().value())};
	searchDrive(folder);
}