const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/product', component: Products, name: 'Products' },
  { path: '/about', component: About, name: 'About' }
];

const router = new VueRouter({
  routes: routes,
  // mode: 'history',
  // base: '/'
})

let app = new Vue({
  el: '#app',
  router: router,
  // data: {
  //   products: [],
  //   showGetModal: false,
  //   showPostModal: false,
  //   selectedProduct: {
  //     id: null,
  //     name: '',
  //     description: '',
  //     price: null,
  //   },
  //   newProduct: {
  //     name: '',
  //     description: '',
  //     price: null,
  //   },
  //   formAction: ''
  // },
  // methods: {
  //   createProduct: function() {
  //     // const url = 'http://192.168.0.105:5000/api/product/create';
  //     const url = `http://localhost:1000/api/product/create_product`;
  //
  //     axios.post(url, this.newProduct)
  //       .then(response => {
  //
  //         console.log(response);
  //
  //         this.showPostModal = false;
  //         this.getAllProducts();
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  //
  //   getAllProducts: function() {
  //     // const url = 'http://192.168.0.105:5000/api/product/read_all'
  //     const url = `http://localhost:1000/api/product/get_products`;
  //
  //     axios.get(url)
  //       .then(response => {
  //         this.products = response.data.data
  //         console.log(this.products);
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  //
  //   getProductById: function(data) {
  //     let id = data.target.value;
  //
  //     // const url = `http://192.168.0.105:5000/api/product/read/${id}`;
  //     const url = `http://localhost:1000/api/product/get_product/${id}`;
  //
  //     axios.get(url)
  //       .then(response => {
  //         this.selectedProduct.id = response.data.data.id;
  //         this.selectedProduct.name = response.data.data.name;
  //         this.selectedProduct.description = response.data.data.description;
  //         this.selectedProduct.price = response.data.data.price;
  //
  //         this.showGetModal = true;
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  //
  //   getProductByIdOnlyData: function(data) {
  //     let id = data.target.value;
  //
  //     // const url = `http://192.168.0.105:5000/api/product/read/${id}`;
  //     const url = `http://localhost:1000/api/product/get_product/${id}`;
  //
  //     axios.get(url)
  //       .then(response => {
  //         this.selectedProduct.id = response.data.data.id;
  //         this.selectedProduct.name = response.data.data.name;
  //         this.selectedProduct.description = response.data.data.description;
  //         this.selectedProduct.price = response.data.data.price;
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  //
  //   updateProductById: function(data) {
  //     let id = data.target.value;
  //
  //     // const url = `http://192.168.0.105:5000/api/product/update/${id}`;
  //     const url = `http://localhost:1000/api/product/update_product/${id}`;
  //
  //     axios.put(url, this.selectedProduct)
  //       .then(response => {
  //         console.log(response);
  //
  //         this.showPostModal = false;
  //         this.getAllProducts();
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  //
  //   deleteProductById: function(data) {
  //     let id = data.target.value;
  //
  //     // const url = `http://192.168.0.105:5000/api/product/delete/${id}`;
  //     const url = `http://localhost:1000/api/product/delete_product/${id}`;
  //
  //     axios.delete(url)
  //       .then(response => {
  //
  //         this.getAllProducts();
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   },
  // },
  // mounted() {
  //   axios.get(`http://localhost:1000/api/product/get_products`)
  //     .then(response => {
  //       this.products = response.data.data
  //     })
  // }
})
