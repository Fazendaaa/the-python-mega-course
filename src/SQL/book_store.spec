# -*- mode: python -*-

block_cipher = None


a = Analysis(['book_store.py'],
             pathex=['/home/farm/Documents/the-python-mega-course/src/SQL'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='book_store',
          debug=False,
          strip=False,
          upx=True,
          console=False )
