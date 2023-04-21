# Created by svetlanalevinsohn at 12/1/19
Feature: Tests for Wiki Search
  # Enter feature description here
  Background:
    Given Tap on search field

  Scenario: User can search and correct result is shown
    When Enter Python to search field
    Then Top result for Python is shown

  Scenario: 'No results found' is shown for no results
    When Enter abirvalg_abirvalg!@# to search field
    Then 'No results found' message is shown