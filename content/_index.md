---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Q-PACER Research Group
      image:
        filename: Q-PACER.png
      text: |
        <br>
        
        The   **Q**uantum, **P**hotonics, **A**ntennas, **C**omputing, **E**mbedded systems, and **R**enewables (**Q-PACER**) Research Group  is a hub of innovation in electronics and photonics research at the Department of EEE, BUET, Bangladesh. Founded and led by [Dr. Sajid Muhaimin Choudhury](author/dr.-sajid-muhaimin-choudhury), the group leverages expertise in both experimental and computational photonics to tackle cutting-edge challenges. 
        


  - block: markdown
    content:
      title: Our Mission
      subtitle: 
      text: Our mission is to advance knowledge in nanophotonics, embedded systems, and quantum computing, and to develop practical technological solutions for society. We aim to solve fundamental and high-impact research questions in photonics and quantum computation while training the next generation of engineers and scientists.
    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
