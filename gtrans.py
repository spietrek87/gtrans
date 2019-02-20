#!/usr/bin/env python3
import os
import sys
import uuid
import shutil
import zipfile

if __name__ == '__main__':

  if len(sys.argv) < 4:
    print("usage %s <directory> <transport_request> \"<description>\"" % os.path.basename(sys.argv[0]))
    print("example: gtrans.py \\\\networkdir\\transports SY1K900123 \"zip_file_name_without_extension\"")
    exit(-1)

  # init
  sd = os.getcwd()        # script directory
  td = sys.argv[1]        # transport directory
  sid = sys.argv[2][:3]   # SID of SAP system
  trn = sys.argv[2][4:]   # transport request Number
  zipname = sys.argv[3]   # name of zip file without extension

  if os.path.isdir(td): # is transport directory available

    if not os.path.isfile(os.path.join(sd, zipname+'.zip')): # do not overwrite other zip files

      tmpd = os.path.join(sd, str(uuid.uuid4()))

      # create temporary folder structure
      if not os.path.isdir(tmpd):

        os.makedirs(tmpd)
        os.makedirs(os.path.join(tmpd, 'cofiles'))
        os.makedirs(os.path.join(tmpd, 'data'))

        cp = os.path.join(td, 'cofiles','K'+trn+'.'+sid)

        if os.path.isfile(cp): # try to copy cofile to temporary folder

          print("copy cofile %s" % cp)
          shutil.copyfile(cp, os.path.join(tmpd,'cofiles','K'+trn+'.'+sid))

          dp = os.path.join(td, 'data','R'+trn+'.'+sid)

          if os.path.isfile(dp): # try to copy data to temporary folder

            print("copy data %s" % dp)
            shutil.copyfile(dp, os.path.join(tmpd,'data','R'+trn+'.'+sid))

            # create zip file
            with zipfile.ZipFile(os.path.join(sd, zipname+'.zip'), 'w', zipfile.ZIP_DEFLATED) as zf:
              print("create %s" % zf.filename)
              for root, dirs, files in os.walk(tmpd):
                for file in files:
                  zf.write(os.path.join(root, file), os.path.join(os.path.basename(os.path.normpath(root)), file))

          else:
            print("data %s not found" % ('R'+trn+'.'+sid))

        else:
          print("cofile %s not found" % ('K'+trn+'.'+sid))

        if os.path.isdir(tmpd): # delete temporary folder
          shutil.rmtree(tmpd)
        print("done")

    else:
      print("zip %s already exists" % os.path.join(sd, zipname+'.zip'))

  else:
    print("directory %s not found" % td)
