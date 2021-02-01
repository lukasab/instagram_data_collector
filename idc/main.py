from env import USERNAME, PASSWORD
from instagram import Instagram

def main():
    insta = Instagram(USERNAME, PASSWORD)
    insta.log_in(is_facebook=True, is_two_factor=True)

if __name__ == '__main__':
    main()