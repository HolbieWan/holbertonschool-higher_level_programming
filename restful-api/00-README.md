# A brief summary explaining the differences between HTTP and HTTPS.

## A depiction or outline of the structure of an HTTP request and response:

## Lists of common HTTP methods with their descriptions and possible use cases:

+ **Method:** GET
<br> **Description:** Retrieves data
<br> **Use case:** Fetching a web page or data from an API.

+ **Method:** POST
<br> **Description:** Create new data
<br> **Use case:** send data to a server to create or update a resource, commonly used for actions that change the server's state like submitting form data or uploading files.

+ **Method:** PUT
<br> **Description:** update or replace an existing resource on the server
<br> **Use case:** modifying specific resources like updating user profiles in web applications.

+ **Method:** DELETE
<br> **Description:** request the removal of a resource on the server. delete specific resources identified by a URI (Uniform Resource Identifier).
<br> **Use case:** employed when a client needs to delete a specific resource identified by a URI.

## List status codes with their descriptions and possible use cases:

+ **Status Code: 404**
<br> **Description:** Not Found
<br> **Scenario:** When a requested page or resource isn’t available on the server.

+ **Status Code: 404**
<br> **Description:** Not Found
<br> **Scenario:** When a requested page or resource isn’t available on the server.

+ **Status Code:200 OK:**
<br> **Description:** The request has succeeded.
<br> **Scenario:** It is commonly returned for successful GET or POST requests.

+ **Status Code: 201 Created:**
<br>**Description:** The request has been fulfilled and a new resource has been created.
<br>**Scenario:** Used when a resource is successfully created, e.g., after a successful POST request.

+ **Status Code:204 No Content:**
<br>**Description:** The server has successfully fulfilled the request, but there is no content to send back.
<br>**Scenario:** Often used in conjunction with DELETE requests to indicate successful deletion.

+ **Status Code: 400 Bad Request:**
<br>**Description:** The server could not understand the request due to invalid syntax.
<br>**Scenario:** Occurs when the client sends a malformed request, such as missing required parameters.

+ **Status Code: 401 Unauthorized:**
<br>**Description:** The request requires user authentication.
<br>**Scenario:** Sent when the client needs to provide credentials or is not authenticated to access a resource.

+ **Status Code:403 Forbidden:**
<br>**Description:** The server understood the request but refuses to authorize it.
<br>**Scenario:** Indicates that the client does not have permission to access the requested resource.

+ **Status Code: 405 Method Not Allowed:**
<br>**Description:** The method specified in the request is not allowed for the resource.
<br>**Scenario:** Sent when the client uses an unsupported HTTP method for a particular resource.

+ **Status Code: 500 Internal Server Error:**
<br>**Description:** The server encountered an unexpected condition that prevented it from fulfilling the request.
<br>**Scenario:** Indicates a generic error on the server side, often due to a misconfiguration or unexpected exception.

+ **Status Code: 503 Service Unavailable:**
<br>**Description:** The server is currently unable to handle the request due to temporary overloading or maintenance.
<br>**Scenario:** Used to indicate that the server is temporarily unable to handle the request, possibly due to high load or maintenance activities.