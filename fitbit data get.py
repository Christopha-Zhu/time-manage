import fitbit
unauth_client = fitbit.Fitbit('22D82M', '3133565ad3c5fed36062355f2f0d29a2')
# certain methods do not require user keys
unauth_client.food_units()
