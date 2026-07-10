is_loggedd_in = True
is_admin = True

if is_loggedd_in:
    print("User is logged in ")
    if is_admin:
        print("show admin panel")
    else:
        print("show regular dashboard")
else:
    print("redirect to login page")