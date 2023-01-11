Sample excel file to test: https://go.microsoft.com/fwlink/?LinkID=521962


```shell
➜  sha256sum flask-app/Financial\ Sample.xlsx 
c3f17156ab7c192571ecfc742e88c16a4b7243a4d4b4a420fcb68dec44e10196  flask-app/Financial Sample.xlsx
```

```shell
➜  docker build --tag dumlu/envoy-502-upe flask-app/                                                                                
Sending build context to Docker daemon  90.11kB
Step 1/6 : FROM python:3.8-slim-buster
 ---> 6ba145ad2ad6
Step 2/6 : WORKDIR /python-docker
 ---> Using cache
 ---> 8825e5fe3347
Step 3/6 : COPY requirements.txt requirements.txt
 ---> Using cache
 ---> a842d0e4d60c
Step 4/6 : RUN pip3 install -r requirements.txt
 ---> Using cache
 ---> fe82b1564bd5
Step 5/6 : COPY . .
 ---> 6ea6ff328ea8
Step 6/6 : CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
 ---> Running in 020efe648b35
Removing intermediate container 020efe648b35
 ---> 21743bb410e7
Successfully built 21743bb410e7
Successfully tagged dumlu/envoy-502-upe:latest
```


```shell
➜  docker push dumlu/envoy-502-upe
Using default tag: latest
The push refers to repository [docker.io/dumlu/envoy-502-upe]
7522e26d3ca4: Pushed
3bc993fbc72b: Mounted from dumlu/envoy-502-upe
b00eb6350316: Mounted from dumlu/envoy-502-upe
f1059028fa78: Mounted from dumlu/envoy-502-upe
ade4cdb42598: Mounted from dumlu/envoy-502-upe
a3af7ad05be9: Mounted from dumlu/envoy-502-upe
b42c4e0a74fd: Mounted from dumlu/envoy-502-upe
9a771a2f7675: Mounted from dumlu/envoy-502-upe
7b6f75f8765b: Mounted from dumlu/envoy-502-upe
latest: digest: sha256:2e08c42b40355cd26569245ec944bb2ff402475cb09f117ed58dcd71f305a3fe size: 2204
```


```s
➜ k get pod -l app=envoy-502-upe                                                                                                 
NAME                             READY   STATUS    RESTARTS   AGE
envoy-502-upe-85646cdc74-6rjf2   2/2     Running   0          26s


➜ k describe pod envoy-502-upe-85646cdc74-6rjf2

Name:         envoy-502-upe-85646cdc74-6rjf2
Namespace:    default
Priority:     0
Node:         test-worker2/10.238.129.106
Start Time:   Wed, 11 Jan 2023 14:30:07 +0300
Labels:       app=envoy-502-upe
              pod-template-hash=85646cdc74
              security.istio.io/tlsMode=istio
              service.istio.io/canonical-name=envoy-502-upe
              service.istio.io/canonical-revision=latest
              sidecar.istio.io/inject=true
Annotations:  cni.projectcalico.org/podIP: 10.42.5.156/32
              cni.projectcalico.org/podIPs: 10.42.5.156/32
              kubectl.kubernetes.io/default-container: envoy-502-upe
              kubectl.kubernetes.io/default-logs-container: envoy-502-upe
              prometheus.io/path: /stats/prometheus
              prometheus.io/port: 15020
              prometheus.io/scrape: true
              sidecar.istio.io/status:
                {"initContainers":["istio-init"],"containers":["istio-proxy"],"volumes":["istio-envoy","istio-data","istio-podinfo","istiod-ca-cert"],"ima...
Status:       Running
IP:           10.42.5.156
IPs:
  IP:           10.42.5.156
Controlled By:  ReplicaSet/envoy-502-upe-85646cdc74
Init Containers:
  istio-init:
    Container ID:  docker://0511183e721169b05376376ff376635d968d1c422dda343100c7d612cd2a8920
    Image:         rancher/mirrored-istio-proxyv2:1.11.7
    Image ID:      docker-pullable://rancher/mirrored-istio-proxyv2@sha256:2a3a41755884efe10f822bcf3474d3fd7d165789184e1a4db70a3ae321838c56
    Port:          <none>
    Host Port:     <none>
    Args:
      istio-iptables
      -p
      15001
      -z
      15006
      -u
      1337
      -m
      REDIRECT
      -i
      *
      -x
      
      -b
      *
      -d
      15090,15021,15020
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Wed, 11 Jan 2023 14:30:08 +0300
      Finished:     Wed, 11 Jan 2023 14:30:08 +0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  1Gi
    Requests:
      cpu:        100m
      memory:     128Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-8924z (ro)
Containers:
  envoy-502-upe:
    Container ID:   docker://cf60270fdc45f9ee4a74494333f05aff211833e9113a2aa5f51dcec7e05d72d0
    Image:          dumlu/envoy-502-upe:latest
    Image ID:       docker-pullable://dumlu/envoy-502-upe@sha256:66faaa945b4b4779602b22e6eba802ad0c09277a4e350e0b1a551fe334487481
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 11 Jan 2023 14:30:15 +0300
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-8924z (ro)
  istio-proxy:
    Container ID:  docker://08473e8b002363c7b7aa3b1c55db170443718a1fe5ec6b47d88b6a41572f5475
    Image:         rancher/mirrored-istio-proxyv2:1.11.7
    Image ID:      docker-pullable://rancher/mirrored-istio-proxyv2@sha256:2a3a41755884efe10f822bcf3474d3fd7d165789184e1a4db70a3ae321838c56
    Port:          15090/TCP
    Host Port:     0/TCP
    Args:
      proxy
      sidecar
      --domain
      $(POD_NAMESPACE).svc.cluster.local
      --proxyLogLevel=warning
      --proxyComponentLogLevel=misc:error
      --log_output_level=default:info
      --concurrency
      2
    State:          Running
      Started:      Wed, 11 Jan 2023 14:30:15 +0300
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  1Gi
    Requests:
      cpu:      100m
      memory:   128Mi
    Readiness:  http-get http://:15021/healthz/ready delay=1s timeout=3s period=2s #success=1 #failure=30
    Environment:
      JWT_POLICY:                    first-party-jwt
      PILOT_CERT_PROVIDER:           istiod
      CA_ADDR:                       istiod.istio-system.svc:15012
      POD_NAME:                      envoy-502-upe-85646cdc74-6rjf2 (v1:metadata.name)
      POD_NAMESPACE:                 default (v1:metadata.namespace)
      INSTANCE_IP:                    (v1:status.podIP)
      SERVICE_ACCOUNT:                (v1:spec.serviceAccountName)
      HOST_IP:                        (v1:status.hostIP)
      PROXY_CONFIG:                  {"gatewayTopology":{"numTrustedProxies":2}}
                                     
      ISTIO_META_POD_PORTS:          [
                                         {"name":"http","containerPort":5000,"protocol":"TCP"}
                                     ]
      ISTIO_META_APP_CONTAINERS:     envoy-502-upe
      ISTIO_META_CLUSTER_ID:         Kubernetes
      ISTIO_META_INTERCEPTION_MODE:  REDIRECT
      ISTIO_META_WORKLOAD_NAME:      envoy-502-upe
      ISTIO_META_OWNER:              kubernetes://apis/apps/v1/namespaces/default/deployments/envoy-502-upe
      ISTIO_META_MESH_ID:            cluster.local
      TRUST_DOMAIN:                  cluster.local
    Mounts:
      /etc/istio/pod from istio-podinfo (rw)
      /etc/istio/proxy from istio-envoy (rw)
      /var/lib/istio/data from istio-data (rw)
      /var/run/secrets/istio from istiod-ca-cert (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-8924z (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  istio-envoy:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     Memory
    SizeLimit:  <unset>
  istio-data:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:     
    SizeLimit:  <unset>
  istio-podinfo:
    Type:  DownwardAPI (a volume populated by information about the pod)
    Items:
      metadata.labels -> labels
      metadata.annotations -> annotations
  istiod-ca-cert:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      istio-ca-root-cert
    Optional:  false
  default-token-8924z:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-8924z
    Optional:    false
QoS Class:       Burstable
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  4m49s  default-scheduler  Successfully assigned default/envoy-502-upe-85646cdc74-6rjf2 to datassist-test-worker2
  Normal  Pulled     4m48s  kubelet            Container image "rancher/mirrored-istio-proxyv2:1.11.7" already present on machine
  Normal  Created    4m48s  kubelet            Created container istio-init
  Normal  Started    4m48s  kubelet            Started container istio-init
  Normal  Pulling    4m47s  kubelet            Pulling image "dumlu/envoy-502-upe:latest"
  Normal  Pulled     4m42s  kubelet            Successfully pulled image "dumlu/envoy-502-upe:latest" in 5.442913902s
  Normal  Created    4m42s  kubelet            Created container envoy-502-upe
  Normal  Started    4m41s  kubelet            Started container envoy-502-upe
  Normal  Pulled     4m41s  kubelet            Container image "rancher/mirrored-istio-proxyv2:1.11.7" already present on machine
  Normal  Created    4m41s  kubelet            Created container istio-proxy
  Normal  Started    4m41s  kubelet            Started container istio-proxy

```


run debug container

```s
➜ k run envoy-502-upe-curl --image=curlimages/curl -i --tty -- sh
```


download test /w curl

```s
/tmp $ curl -v -XPOST envoy-502-upe:5000/download-1 -o 1.xlsx
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.43.47.85:5000...
* Connected to envoy-502-upe (10.43.47.85) port 5000 (#0)
> POST /download-1 HTTP/1.1
> Host: envoy-502-upe:5000
> User-Agent: curl/7.87.0-DEV
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< server: envoy
< date: Wed, 11 Jan 2023 12:02:27 GMT
< content-disposition: attachment;filename="Financial Sample.xlsx"
< content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9
< content-length: 83418
< last-modified: Wed, 11 Jan 2023 10:47:04 GMT
< cache-control: no-cache
< x-envoy-upstream-service-time: 40
<
{ [13613 bytes data]
100 83418  100 83418    0     0  1596k      0 --:--:-- --:--:-- --:--:-- 1629k
* Connection #0 to host envoy-502-upe left intact


/tmp $ curl -v -XPOST envoy-502-upe:5000/download-2 -o 2.xlsx
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.43.47.85:5000...
* Connected to envoy-502-upe (10.43.47.85) port 5000 (#0)
> POST /download-2 HTTP/1.1
> Host: envoy-502-upe:5000
> User-Agent: curl/7.87.0-DEV
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< server: envoy
< date: Wed, 11 Jan 2023 12:02:37 GMT
< content-disposition: attachment;filename="Financial Sample.xlsx"
< content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9
< content-length: 83418
< last-modified: Wed, 11 Jan 2023 10:47:04 GMT
< cache-control: no-cache
< x-envoy-upstream-service-time: 5
<
{ [6624 bytes data]
100 83418  100 83418    0     0  10.1M      0 --:--:-- --:--:-- --:--:-- 11.3M
* Connection #0 to host envoy-502-upe left intact


/tmp $ curl -v -XPOST envoy-502-upe:5000/download-3 -o 3.xlsx
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.43.47.85:5000...
* Connected to envoy-502-upe (10.43.47.85) port 5000 (#0)
> POST /download-3 HTTP/1.1
> Host: envoy-502-upe:5000
> User-Agent: curl/7.87.0-DEV
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< server: envoy
< date: Wed, 11 Jan 2023 12:02:44 GMT
< content-disposition: attachment;filename="Vestas Wind System A-S TR Maliyet Raporu 31.10.2022.xlsx"
< content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;;charset=ISO 8859-9
< content-length: 83418
< last-modified: Wed, 11 Jan 2023 10:47:04 GMT
< cache-control: no-cache
< x-envoy-upstream-service-time: 7
<
{ [13579 bytes data]
100 83418  100 83418    0     0  8197k      0 --:--:-- --:--:-- --:--:-- 9051k
* Connection #0 to host envoy-502-upe left intact


/tmp $ curl -v -XPOST envoy-502-upe:5000/download-4 -o 4.xlsx
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 10.43.47.85:5000...
* Connected to envoy-502-upe (10.43.47.85) port 5000 (#0)
> POST /download-4 HTTP/1.1
> Host: envoy-502-upe:5000
> User-Agent: curl/7.87.0-DEV
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 502 Bad Gateway
< content-length: 87
< content-type: text/plain
< date: Wed, 11 Jan 2023 12:02:54 GMT
< server: envoy
< x-envoy-upstream-service-time: 26
<
{ [87 bytes data]
100    87  100    87    0     0   1796      0 --:--:-- --:--:-- --:--:--  1812
* Connection #0 to host envoy-502-upe left intact

```



sample app & sidecar logs:

```s
envoy-502-upe-74b55b9d7-fqz9d envoy-502-upe 127.0.0.6 - - [11/Jan/2023 12:02:27] "POST /download-1 HTTP/1.1" 200 -
envoy-502-upe-74b55b9d7-fqz9d istio-proxy [2023-01-11T12:02:27.565Z] "POST /download-1 HTTP/1.1" 200 - via_upstream - "-" 0 83418 6 5 "-" "curl/7.87.0-DEV" "16ecf80b-2dd5-4597-bb01-823326916615" "envoy-502-upe:5000" "10.42.3.60:5000" inbound|5000|| 127.0.0.6:47351 10.42.3.60:5000 10.42.5.151:46008 outbound_.5000_._.envoy-502-upe.default.svc.cluster.local default

envoy-502-upe-74b55b9d7-fqz9d envoy-502-upe 127.0.0.6 - - [11/Jan/2023 12:02:37] "POST /download-2 HTTP/1.1" 200 -
envoy-502-upe-74b55b9d7-fqz9d istio-proxy [2023-01-11T12:02:37.711Z] "POST /download-2 HTTP/1.1" 200 - via_upstream - "-" 0 83418 3 2 "-" "curl/7.87.0-DEV" "c603ea0a-5157-4a40-9514-eba7bfb9ca39" "envoy-502-upe:5000" "10.42.3.60:5000" inbound|5000|| 127.0.0.6:51923 10.42.3.60:5000 10.42.5.151:46008 outbound_.5000_._.envoy-502-upe.default.svc.cluster.local default

envoy-502-upe-74b55b9d7-fqz9d envoy-502-upe 127.0.0.6 - - [11/Jan/2023 12:02:44] "POST /download-3 HTTP/1.1" 200 -
envoy-502-upe-74b55b9d7-fqz9d istio-proxy [2023-01-11T12:02:44.496Z] "POST /download-3 HTTP/1.1" 200 - via_upstream - "-" 0 83418 3 2 "-" "curl/7.87.0-DEV" "7bb9070a-353b-4378-840c-08c08788bff7" "envoy-502-upe:5000" "10.42.3.60:5000" inbound|5000|| 127.0.0.6:32965 10.42.3.60:5000 10.42.5.151:46992 outbound_.5000_._.envoy-502-upe.default.svc.cluster.local default

envoy-502-upe-74b55b9d7-fqz9d envoy-502-upe 127.0.0.6 - - [11/Jan/2023 12:02:54] "POST /download-4 HTTP/1.1" 200 -
envoy-502-upe-74b55b9d7-fqz9d istio-proxy [2023-01-11T12:02:54.579Z] "POST /download-4 HTTP/1.1" 502 UPE upstream_reset_before_response_started{protocol_error} - "-" 0 87 4 - "-" "curl/7.87.0-DEV" "c51364bd-d43e-4f87-9587-d535a3475d7c" "envoy-502-upe:5000" "10.42.3.60:5000" inbound|5000|| 127.0.0.6:45107 10.42.3.60:5000 10.42.5.151:46992 outbound_.5000_._.envoy-502-upe.default.svc.cluster.local default
```