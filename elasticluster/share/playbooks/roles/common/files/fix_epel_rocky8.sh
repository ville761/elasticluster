#!/bin/bash

   # Update the system
   sudo dnf update -y

   # Remove existing EPEL release package if present
   sudo dnf remove -y epel-release

   # Import the EPEL GPG key
   sudo rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-8

   # Install the EPEL release package
   sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

   # Clean DNF cache
   sudo dnf clean all

   # Refresh the repository metadata
   sudo dnf makecache

   echo "EPEL repository setup complete. Please try your Elasticluster deployment again."
