#!/usr/bin/env python3

# Script Name:                  challenge12.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/12/2023
# Purpose:                      Python requests library
# Additional Source             ChatGPT

import requests

def get_user_input():
    url = input("Enter the destination URL: ")
    http_method = input("Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
    
    return url, http_method

def confirm_request(url, http_method):
    print("\nRequest Details:")
    print(f"URL: {url}")
    print(f"HTTP Method: {http_method}")
    
    confirmation = input("\nDo you want to proceed with the request? (y/n): ").lower()
    
    return confirmation == 'y'

def perform_request(url, http_method):
    try:
        response = requests.request(http_method, url)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
        return None

def translate_status_code(status_code):
    status_codes = {
        200: 'OK',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        500: 'Internal Server Error'
    }
    return status_codes.get(status_code, f'Unknown Status Code: {status_code}')

def print_response_info(response):
    if response:
        print("\nResponse Header Information:")
        print(f"Status Code: {response.status_code} - {translate_status_code(response.status_code)}")
        print("Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    destination_url, http_method = get_user_input()

    if confirm_request(destination_url, http_method):
        response = perform_request(destination_url, http_method)
        print_response_info(response)
    else:
        print("Request aborted.")
