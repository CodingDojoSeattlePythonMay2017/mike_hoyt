# -*- text -*-

Assignment: Dojo Survey

Build a flask application that:
  - accepts a form submission
  - redirects
  - presents the submitted data on a results page

The goal is to help you get familiar with sending POST requests through a form
and displaying that information. Consider the below example as a guide.

Page: .../index.html

                       +--------+
    Your Name:         |...     |
                       +--------+
                       +--------+
    Dojo Location:     |...     |
                       +--------+
                       +--------+
    Favorite Language: |...     |
                       +--------+
    
    Comment (optional):
    +---------------------------+
    | ....                      |
    |                           |
    |                           |
    +---------------------------+
    
    +--------+
    | Submit |
    +--------+

Page: .../results.html

    Submitted Info
    --------------

      Name:              <name>

      Dojo Location:     <loc>

      Favorite Language: <lang>

      Comment:           <comment>

    +---------+
    | Go Back |
    +---------+

Hint: Although we've told you never to render from a post route, you'll need to
do so for this assignment. We'll show you tools to avoid doing so soon.

