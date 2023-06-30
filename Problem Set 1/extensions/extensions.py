suffix = input("File name: ").strip().lower().split(".")

suffix = suffix[-1]

if  suffix == "gif":
    print("image/gif")

elif suffix == "jpg":
    print("image/jpeg" )

elif suffix == "jpeg":
    print("image/jpeg" )

elif suffix == "png":
    print("image/png" )

elif suffix == "pdf":
    print("application/pdf")

elif suffix == "txt":
    print("text/plain")

elif suffix == "zip":
    print("application/zip" )
else:
    print("application/octet-stream" )

