# IBM z/OS CICS collection

The **IBM® z/OS® CICS® collection**, also represented as **ibm\_zos\_cics**
in this document, is part of the broader initiative to bring Ansible Automation to IBM Z® through the offering
**Red Hat® Ansible Certified Content for IBM Z®**. The **IBM z/OS CICS collection** supports management of CICS
resources and definitions through the CMCI REST API provided by CICS as well as provisioning of standalone CICS regions.

This CICS collection works in conjunction with other Ansible collections for IBM Z,
such as the [IBM z/OS core collection](https://github.com/ansible-collections/ibm_zos_core).
It is also possible to use it independently to perform automation tasks solely in CICS.


## Red Hat Ansible Certified Content for IBM Z

**Red Hat® Ansible Certified Content for IBM Z** provides the ability to
connect IBM Z® to clients' wider enterprise automation strategy through the
Ansible Automation Platform ecosystem. This enables development and operations
automation on Z through a seamless, unified workflow orchestration with
configuration management, provisioning, and application deployment in
one easy-to-use platform.

The **IBM z/OS CICS collection** is following the
**Red Hat® Ansible Certified Content for IBM Z®** method of distributing
content. Collections will be developed in the open, and when content is ready
for use it is released to
[Ansible Galaxy](https://galaxy.ansible.com/search?keywords=zos_&order_by=-relevance&deprecated=false&type=collection&page=1)
for community adoption. Once contributors review community usage, feedback,
and are satisfied with the content published, the collection will then be
released to [Ansible Automation Hub](https://www.ansible.com/products/automation-hub)
as **certified** and **IBM supported** for
**Red Hat® Ansible Automation Platform subscribers**. 


For guides and reference, please review the [documentation](https://ibm.github.io/z_ansible_collections_doc/index.html).

## Features

The IBM CICS collection includes
[modules](https://ibm.github.io/z_ansible_collections_doc/ibm_zos_cics/docs/source/modules.html),
[sample playbooks](https://github.com/IBM/z_ansible_collections_samples),
and ansible-doc to:

- Automate tasks in CICS.
- Provision or deprovision CICS regions.
- Start or stop a CICS region.

  
## Installation


You can install this collection with the Ansible Galaxy command-line tool:
```sh
ansible-galaxy collection install ibm.ibm_zos_cics
```


You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:
```sh
collections:
  - name: ibm.ibm_zos_cics
```


To install a specific version of the collection or upgrade an an existing installation to a specific version, for example installing 2.1.0, use the following syntax:
```sh
ansible-galaxy collection install ibm.ibm_zos_cics:2.1.0
```


If you want to upgrade the collection to the latest version, you can run:
```sh
ansible-galaxy collection install ibm.ibm_zos_cics --upgrade
```

## Use Cases

* Use Case Name: Provision region data sets
  * Actors:
    * System Programmer
  * Description:
    * A system programmer can provision a set of region data sets such as the Global Catalog data set, Local Catalog data 
      set and CSD data set.
  * Flow:
    * abc
* Use Case Name: Deprovision region data sets
  * Actors:
    * System Programmer
  * Description:
    * A system programmer can deprovision a set of region data sets such as the Global Catalog data set, Local Catalog data 
      set and CSD data set.
  * Flow:
    * abc
* Use Case Name: Start a CICS region
  * Actors:
    * System Programmer
  * Description:
    * A system programmer can start a CICS region with their provisioned region data sets
  * Flow:
    * Verify they have provisioned the region data sets correctly.
    * 



## Release Notes and Roadmap


## Contributing

We welcome contributions! Find out how in our [contribution guide](https://github.com/ansible-collections/ibm_zos_cics/blob/main/CONTRIBUTING.md).

## Copyright 

© Copyright IBM Corporation 2021, 2024.

## License

This collection is licensed under the [Apache License,
Version 2.0](https://opensource.org/licenses/Apache-2.0).
