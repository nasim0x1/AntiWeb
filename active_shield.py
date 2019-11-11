import data_list
hosts_path = data_list.hosts_path
redirect = "127.0.0.1"
website_list = data_list.website_list
def active():
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

active()
