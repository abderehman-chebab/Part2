import requests  # Import the library for making HTTP requests.

def http_request(url='https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1', max_retries=5):
    """
    This function sends an HTTP GET request to the specified URL and retries if it fails.

    Args:
        url (str, optional): The URL to send the request to. Defaults to the example API endpoint.
        max_retries (int, optional): The maximum number of retry attempts. Defaults to 5.

    Returns:
        str: A message indicating the success or failure of the request.
    """

    retries = 0  # Initialize a counter for retry attempts.

    while retries < max_retries:  # Loop until success or max retries reached.
        try:
            response = requests.get(url)  # Send the HTTP GET request.
            response.raise_for_status()  # Check for HTTP errors (4xx, 5xx). Raise an exception if found.

            data = response.json()  # Parse the JSON response from the server.

            if data == {"message": "success"}:  # Check if the response matches the expected result.
                return "Success! The request returned the expected JSON response."  # Return success message.
            else:
                return f"Request failed. Unexpected JSON response: {data}"  # Return error message with details.

        except requests.exceptions.RequestException as e:  # Catch any exceptions during the request.
            retries += 1  # Increment the retry counter.

            if retries < max_retries:  # If retries are left, print a retry message.
                print(f"Request attempt {retries} failed: {e}. Retrying...")
            else:  # If all retries are exhausted, return a final error message.
                return f"Request failed after {max_retries} attempts: {e}"


# Example Usage:
result = http_request()  # Call the function (using the default URL and retry settings).
print(result)  # Print the result of the request




