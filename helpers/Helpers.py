import re 

class ToolHelper:

    @staticmethod
    def slugify(string):
       
        string = string.lower()
        
        string = re.sub(r'[^\w\s-]', '', string).strip()
        string = re.sub(r'[-\s]+', '-', string)
        
        return string
    
    @staticmethod
    def verify_link_hash(link, search_link):

        verify_link_content = link.find('https://') != -1 or link.find('http://') != -1

        if not verify_link_content:
            
            verify_link = search_link

            verify_https = verify_link.find('https://') != -1 

            pattern = re.compile(r'^(http|ftp)s?://')
            clean_url = re.sub(pattern, '', verify_link)
            
            verify_link = clean_url.split('/')[0]

            if verify_https:
                verify_link = 'https://' + verify_link + link
            else:
                verify_link = 'http://' + verify_link + link

            return verify_link
        
        return link


            