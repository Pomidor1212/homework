import messages

# NAME INPUT
name = input(messages.MSG_INPUT_NAME)
name = name.strip()

if name.isalpha():
    name = name.title()
    print(messages.MSG_NAME_OK.format(name=name))
else:
    print(messages.MSG_NAME_ERROR)

# AGE INPUT
age = input(messages.MSG_INPUT_AGE)
age = age.strip()
age = age.lstrip("0")

if age.isdigit():
    print(messages.MSG_AGE_OK.format(age=age))
else:
    print(messages.MSG_AGE_ERROR)

# PHONE INPUT
phone = input(messages.MSG_INPUT_PHONE)
phone = phone.strip()

if phone.isdigit():
    print(messages.MSG_PHONE_OK.format(phone=phone))
else:
    print(MSG_PHONE_ERROR)

print(messages.MSG_FINISH)
