# hit400
The official repository for my HIT400 project

## Topic: Leveraging IOCs for effective Cyber Threat Intelligence in tertiary institutions

Link to literature review: https://docs.google.com/document/d/1ifD8otspq4xvXUsX06bWL6ex-r88D2OfDlC8b1c7koo/edit#

## Project References
- Protective: https://gitlab.com/protective-h2020-eu/protective-node/wikis/description/system-overview
- Warden: https://warden.cesnet.cz/en/index

## Tools
- STIX: https://stixproject.github.io/ (https://oasis-open.github.io/cti-documentation/)
- TAXII: https://taxiiproject.github.io/
- stix2viz
  

# what is this?

The threat intelligence platform is meant to enhance the way institutions share threat information and "current" indicators of compromise. It is a peer to peer network where members have the ability to view as well as share information on threats. The system updates in real time, making it effective for users to keep track of what is currently taking place.

## TIP goals

- to collect logs from different applications on the host
- to analyze those logs, set a threshhold and only share what can be defined in security as an "incident"
- to be able to share indicators of compromise**format to be reviewed
- to upload stix2 content or json files and visualize the objects and better understand them
- to be able to view and share TIP updates in real time

## Explicit goals

1. To collect logs

- so we want to make sure that we include incidents or threats that target institutions in our geographical location. We want to be able to relate to whatever is being shared on the platform. Hence, the collection of host logs. This includes system logs and application logs, mostly the ones that matter
- to achieve this i will be using osquery: this applies for Linux based amchines

2. To analyze logs

- okay, so we've collected logs, what do we do with them. I'ts tiring to go through logs line by line because there are always thousands of lines. And we also want to make sure that the information that we're sharing is relevant. Here we want to analyze the logs and single out indicators of compromise from them that cause a certain disruption. This means that it must be defined as an incident of some sort, otherwise we'll be sharing too much useless information. So we're going to set threshholds, as to what exactly can be defined as an incident
- for example: bruteforce attempts that can bring down the servers for some time, we share the source ip and everything related
- to achieve this i will be using Python i think, idk, we'll see

3. Sharing indicators of compromise

- after experiencing some sort of incident, we then want to be able to share information about that event with our peers
- so whoever is sharing must provide a detailed description of the IOC and what to watch out for
- sharing will be happening on the taxii server

4. To upload stix2 content

- so we also want our users to be up to date with what is happening to other institutions, those not in their own geographical location
- to do this, we allow users to obtain stix2 content from other sources and be able to upload that to our system
- this way they can vusualize the threat actors and gain more insight of what they can watch out for as well
- this will also be shared on the taxii server
- visualization is being done using stix2viz


5. Peer to peer

- to bundle it u, the system must be a peer to peer network. It must allow it's users to get updates being shared in real time
