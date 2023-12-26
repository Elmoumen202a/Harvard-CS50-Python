mesg=input("File Name: ")
mesgg = mesg.lower()
# pdf or zip print "application/type of file
if ".pdf" in mesgg :
    print("application/pdf")
elif ".zip" in mesgg:
    print("application/zip")
# if it is text print plain/type
elif ".txt" in mesgg:
    print("text/plain")
# all type of image print "image/type of file
elif ".gif" in mesgg :
    print("image/gif")
elif ".jpeg" in mesgg :
    print("image/jpeg")
elif ".jpg" in mesgg :
    print("image/jpeg")
elif ".png" in mesgg :
    print("image/png")
# else print application/octet-stream
else:
    print("application/octet-stream")



