# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None
hidden_imports = collect_submodules('pyttsx3')


a = Analysis(['C:\\Users\\HP\\PycharmProjects\\ZED Mp3 player\\scripts\\MusicApp.py'],
             pathex=['C:\\Users\\HP\\PycharmProjects\\ZED Mp3 player'],
             binaries=[],
             datas=[],
             hiddenimports=hidden_imports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MusicApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\HP\\PycharmProjects\\ZED Mp3 player\\assets\\Wwalczyszyn-Android-Style-Music-Player.ico')
