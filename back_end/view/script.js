const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/classifier', component: Classifier, name: 'Classifier' },
  { path: '/warehouse', component: Warehouse, name: 'Warehouse' },
  { path: '/supplier', component: Supplier, name: 'Supplier' },
  { path: '/seller', component: Seller, name: 'Seller' },
  { path: '/product', component: Product, name: 'Product' },
  { path: '/about', component: About, name: 'About' }
];

const router = new VueRouter({
  routes: routes,
  // mode: 'history',
  base: '/'
})

let app = new Vue({
  el: '#app',
  router: router
})
