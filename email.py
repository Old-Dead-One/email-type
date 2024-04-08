class Email:
    def __init__(self, content: str):
        if not isinstance(content, str):
            raise TypeError("Please provide a valid email address.")
        
        if "@" not in content:
            raise TypeError("Please provide a valid email address.")
 
        valid_tlds: list[str] = [".com", ".net", ".edu", ".org"]
        tld = content[-4:]
        if tld not in valid_tlds:
            raise TypeError("Please provide a valid email address.")

        domain_start = content.find("@") + 1
        domain = content[at_sign_index:-4]
        if domain == ""
            raise TypeError("Please provide a valid email address.")

        if content.find("@") == 0:
            raise TypeError("Please provide a valid email address.")



    self.content = content
    def __str__(self) -> str:
        return self.content
