---
title: System Demonstrations
layout: single
excerpt: "Accepted System Demonstration Papers of ACL 2026"
permalink: /program/demo/
sidebar:
  nav: "program"
---

{% for paper in site.data.papers_demo %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}
