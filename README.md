# Prometheus Alertmanager to OMI

 - Settings are passed as environment vars:  
        OMI_URL: The OMI url that will receive the alerts.  
        OMI_CATEGORY: OMI category to send in the event.  
        OMI_CI: OMI CI to send with in the event  
 - Template is in template.xml. It uses jinja.
 - You can run this app inside of openshift with oc new-app.
 - Includes omireceiver as a dummy-service to receive the events and make some tests.

## Example
### Install:
```bash
oc create ns alertman2omi  
oc -n alertman2omi new-app https://github.com/jmgarciac/alertman2omi.git --context-dir=app --name alertman2omi \
 -e OMI_URL="http://omireceiver.alertman2omi.svc:8080/post" \
 -e OMI_CATEGORY="OPENSHIFT" \
 -e OMI_CI="poc-ocp4"  
```

### Uninstall alertman2omi
```bash
oc -n alertman2omi delete all -l app=alertman2omi
oc delete ns alertman2omi
```

### Install dummy omireceiver (only for testing)  
```bash
oc -n alertman2omi new-app  https://github.com/jmgarciac/alertman2omi.git --context-dir=omireceiver/app --name omireceiver
```

### Uninstall dummy omireceiver
```bash
oc -n alertman2omi delete all -l app=omireceiver
```