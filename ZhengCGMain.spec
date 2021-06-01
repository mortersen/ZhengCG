# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

SETUP_DIR = 'C:\\MyProject\\ZhengCG\\'


a = Analysis(['ZhengCGMain.py',
              'DBTreeView.py',
              'PDFWidget.py',
              'RecordDetailView.py',
              'SearchView.py',
              'C:\\MyProject\\ZhengCG\\RES\\img_rc.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_AboutDialog.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_DBTreeWidget.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_DetailWidget.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_IndexWidget.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_MainWindow.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_ReadPDF.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_RecordDetailView.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_SearchWidget.py',
              'C:\\MyProject\\ZhengCG\\UI\\UI_TableViewWidget.py',
            ],
             pathex=['C:\\MyProject\\ZhengCG'],
             binaries=[],
             datas=[(SETUP_DIR+'DB\\','DB\\')],
             hiddenimports=['sys','os','fitz','queue','PyQt5','threading','multiprocessing','tempfile','win32api','win32print'],
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
          [],
          exclude_binaries=True,
          name='郑成功文献数据库',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon='CG.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='郑成功文献数据库')