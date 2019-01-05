import urllib.request as ur
def profanityAlert(path_file):
    file_check = open(path_file)
    content = file_check.read()
    file_check.close()
    try:
        response = ur.urlopen("http://www.wdylike.appspot.com/?q=%s"%(ur.quote(content)))
        output = bool(response.read())
        response.close()
    except:
        print("The detector api must be down. Try after some time")

    if output == True:
        print("Profanity Alert !!")
    else:
        print("No Profanities found.")



profanityAlert(r"Example.txt")