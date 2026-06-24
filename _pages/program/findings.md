---
title: Accepted Findings Papers
layout: single
excerpt: "Accepted Findings Papers of ACL 2026"
permalink: /program/findings/
sidebar:
  nav: "program"
---

{% for paper in site.data.papers_findings %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}
