errors = 2
info = 1

def notify_user():
  print(f"Errors: {errors} | Info: {info}")

def error_handler():
  print("Errors are not yet handled.")

if __name__ == "__main__":
  notify_user()

  # Note: need to handle errors
  error_handler()
