---
title: "Service Life Time"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Differences Between Scoped, Transient, And Singleton Service In .Net Core

Services can be registered with one of the following lifetimes:

- Transient
- Scoped
- Singleton

{{< columns >}}

## Transient

Transient lifetime services are created each time they're requested from the service container.  
This lifetime works best for lightweight, stateless services.
<--->

## Scoped

For web applications, a scoped lifetime indicates that services are created once per client request (connection).

{{</ columns >}}

## Singleton

Singleton lifetime services are created either:

- The first time they're requested.
- By the developer, when providing an implementation instance directly to the container. This approach is rarely needed.

Every subsequent request of the service implementation from the dependency injection container uses the same instance.  
If the app requires singleton behavior, allow the service container to manage the service's lifetime.

Singleton services must be thread safe and are often used in stateless services.

In apps that process requests, singleton services are disposed when the ServiceProvider is disposed on application shutdown. Because memory is not released until the app is shut down, consider memory use with a singleton service.

{{< hint warning >}}
**Do not resolve a more long-live service in a short-live service, and be careful not to do so indirectly.**

for example, through a transient service. It may cause the service to have incorrect state when processing subsequent requests.  
It's fine to:

- Resolve a singleton service from a scoped or transient service.
- Resolve a scoped service from another scoped or transient service.

{{< /hint >}}
