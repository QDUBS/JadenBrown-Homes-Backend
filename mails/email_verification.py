import os
from dotenv import load_dotenv

load_dotenv()
host_url = os.environ.get("HOST_URL")


def email_verification_html(token): 
  html= f"""

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@600;700&family=Roboto+Condensed:wght@300;400;700&display=swap"
          rel="stylesheet"
        />
        <title>MarksFidel | Email Verification</title>
      </head>
      <body
        style="
          padding: 6px;
          border-radius: 4px;
          max-width: 960px;
          margin: 0 auto;
          background-color: rgb(4, 2, 41);
          width: 100%;
          color: white;
        "
      >
        <h1
          class="title"
          style="
            color: #fdfdfd;
            text-align: center;
            padding: 10px 0;
            font-family: Roboto Condensed, sans-serif;
          "
        >
          Verify Email
        </h1>
        <p
          class="message"
          style="
            line-height: 1.7em;
            color: #fcfafa;
            font-size: 16px;
            padding: 10px;
            font-family: Roboto Condensed, sans-serif;
          "
        >
          Hi, <br />
          <br />Thank you for registering with MarksFidel Integrated Services.
          <br />
          To ensure the security of your account and activate all features, please
          verify your email address by clicking on the link below
        </p>

        <a
          href="{host_url}/auth/token/{token}"
          class="button"
          style="
            background-color: rgb(70, 70, 146);
            color: #fff;
            font-size: 16px;
            padding: 8px 10px;
            border-radius: 6px;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            margin-left: 10px;
            text-decoration: none;
            font-family: Roboto Condensed, sans-serif;
          "
          >Verify Email
        </a>
        <p
          class="message"
          style="
            line-height: 1.3em;
            color: #faf6f6;
            font-size: 16px;
            padding: 10px;
            font-family: Roboto Condensed, sans-serif;
          "
        >
          If you are unable to click on the link, please copy and paste it into your
          web browser.
        </p>
        <p
          class="message"
          style="
            line-height: 1.3em;
            color: #ffffff;
            font-size: 16px;
            padding: 10px;
            font-family: Roboto Condensed, sans-serif;
          "
        >
          Please note that this link is valid for the next 24 hours. If you did not
          sign up for , please disregard this email. <br />
          <br />Thank you for choosing MarksFidel Integrated Services! <br />
          <br /><br />Best regards
        </p>
      </body>
    </html>

    """ 
  return html
