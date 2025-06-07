def shutdown(input_str):
    if input_str == "Yes":
        return "Shutting down"
    elif input_str == "no":
        return "Abort shut down"
    else:
        return "Sorry"

# Example usage
user_input = input("Do you want to shut down the system? (Yes/no): ")
result = shutdown(user_input)
print(result)
