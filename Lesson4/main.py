from website_alive import check_response
from website_alive import make_request


def main():
    # url=input("write url: ")
    url = "https://api.github.com"
    site = check_response.foo_site(url)
    print(make_request.foo_answer(site))


main()
