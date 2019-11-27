# Prometheus Alertmanager to HP Omi

 - Settings are passed as environment vars:  
        OMI_URL: The OMI url that will receive the alerts.  
        OMI_CATEGORY: OMI category to send in the event.  
        OMI__CI: OMI CI to send with in the event  
 - Template is in template.xml. It uses jinja.
 - You can run this app inside of openshift with oc new-app.
 - Includes omireceiver as a dummy-service to receive the events and make some tests.

## Example
### Install:
```
oc create ns alertman2omi  
oc -n alertman2omi new-app https://github.com/jmgarciac/alertman2omi.git --context-dir=omireceiver/app --name omireceiver  
oc -n alertman2omi new-app https://github.com/jmgarciac/alertman2omi.git --context-dir=app --name alertman2omi \
 -e OMI_URL="http://omireceiver.alertman2omi.svc:8080/post" \
 -e OMI_CATEGORY="INCIDENT"\
 -e OMI_CI="OpenShift_POC"  
```
### Uninstall
```
oc delete ns alertman2omi  
oc -n alertman2omi delete all -l app=omireceiver
oc -n alertman2omi delete all -l app=alertman2omi
```