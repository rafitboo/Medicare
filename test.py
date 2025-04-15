from werkzeug.security import check_password_hash
hashed_password = 'hashed_password_from_database'
print(check_password_hash(hashed_password, 'plain_text_password'))