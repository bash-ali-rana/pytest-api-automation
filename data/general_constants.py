# CONFIG FILE
PROPERTIES_FILE = "config/properties.ini"

# AUTH INFORMATION
AUTH_ROUTE = "https://auth.routee.net/oauth/token"
GRANT_TYPE = 'grant_type=client_credentials&scope=sms'
BASIC_KEY = 'Basic NjExZDZjMDU3YTg0ZWUwMDAxMzQzYWU1Ok9WYklnOEF2RlE='

# ENDPOINTS
SMS_ENDPOINT = "sms"

# DATA
SMS_PAYLOAD = {
    "body": "A new game has been posted to the MindPuzzle. Check it out",
    "from": "+306999999999",
    "to": "+306911111111"
}
BAD_SMS_PAYLOAD = {
    "body": "A new game has been posted to the MindPuzzle. Check it out",
    "to": "+306911111111"
}
EXPIRED_TOKEN = {
    "Authorization": "Bearer 6fca530f-8353-4e6f-90ce-10a74c99b910"
}

# ERROR MESSAGES
MSGS_INSUFFICIENT_BALANCE = "Insufficient Balance"
MSSG_INTERNAL_SERVER_ERROR = "Internal Server Error"
MSSG_INVALID_TOKEN = "invalid_token"
