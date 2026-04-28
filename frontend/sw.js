self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          return caches.delete(cacheName);
        })
      );
    })
  );
  self.registration.unregister();
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  // Pass through all requests directly to the network
  event.respondWith(fetch(event.request));
});
