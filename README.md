# EmailNotificationForStock
A simple email notifier that sends an email to any desired email addresses when stock reaches a specified target.

Might be helpful for those people tracking GME, AMC but can't set a sell price because application won't let you set it at more than 50% the current price.

Steps to make it work:
1. Create an burnable gmail address and turn on "Less Secure Access"
2. Install python, selenium, firefox (for windows user, install geckdriver for Windows, put it in PATH)
3. Create a file called "email_list.py" that contains two things:
     ```
     EMAIL_LIST = ["email.receiving1@gmail.com", "email.receiving2@gmail.com]
     FROM_MAIL = "email.that.is.sending@gmail.com"
     ```
4. Set your sell point:
     ```
     TARGET_SALE_PRICE = "5000"  # diamond hands
     ```
5. Run the server and sit back til you get your email.
