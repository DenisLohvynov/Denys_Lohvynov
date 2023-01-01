Feature: test Dropbox API
    Scenario: POST
        Given Dropbox API
        When Send request to Dropbox to upload file
        Then Receive response about successful operation
    
    Scenario: GET
        Given Dropbox API with the access to a file
        When Send request to Dropbox to recieve file's metadata
        Then Receive response with
    
    Scenario: DELETE
        Given Dropbox API with the access to a file
        When Send request to Dropbox to delete file
        Then Receive response about successful deletion
