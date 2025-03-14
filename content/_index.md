

---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: resume-biography
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text:
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: ECE.jpg
          filters:
            brightness: 0.6
          size: cover
          position: center
          parallax: false

  - block: markdown
    content:
      title: 'Welcome 👋'
      subtitle: ''
      text: |-
        Hello, I am [Dr. Sajid Muhaimin Choudhury](/about) (ডঃ সাজিদ মুহাইমিন চৌধুরী), working as an Associate Professor in the Department of EEE, BUET. This is my website.
        Please feel free to browse through the links to know more about my [research](/research), [publications](publication). Whether you are a prospective student, potential collaborator, fellow researcher, or just interested regarding my research, please feel free to [contact me](/contact-info). 
        **Note** If you are seeking a Letter of Recommendation from me, kindly visit [this page](/outreach/LOR).
    design:
      columns: '1'
  - block: collection
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: post
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: date-title-summary
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
