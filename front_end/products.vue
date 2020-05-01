const Products  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      products: [],
      showGetModal: false,
      showPostModal: false,
      selectedProduct: {
        _id: null,
        sku: '',
        title: '',
        description: '',
        type: '',
        price: null
      },
      newProduct: {
        sku: '',
        title: '',
        description: '',
        type: '',
        price: null
      },
      formAction: ''
    }
  },
  methods: {
    showActionText: function(action) {
      if (action === 'success') {
        this.showSuccessText = true;

        setTimeout(function() {
          this.showSuccessText = false;
        }.bind(this), 2000);
      }

      if (action === 'error') {
        this.showErrorText = true;

        setTimeout(function() {
          this.showErrorText = false;
        }.bind(this), 2000);
      }

      if (action === 'warning') {
        this.showWarningText = true;

        setTimeout(function() {
          this.showWarningText = false;
        }.bind(this), 2000);
      }
    },

    createProduct: function() {
      // const url = 'http://192.168.0.105:5000/api/product/create';
      const url = `http://localhost:1000/api/product/create_product`;

      axios.post(url, this.newProduct)
        .then(response => {

          console.log(response);

          this.showPostModal = false;
          this.getAllProducts();
          this.showActionText('success');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllProducts: function() {
      // const url = 'http://192.168.0.105:5000/api/product/read_all'
      const url = `http://localhost:1000/api/product/get_products`;

      this.loading = true;

      axios.get(url)
        .then(response => {
          this.products = response.data.data
          console.log(this.products);

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getProductById: function(data) {
      let id = data.target.value;

      // const url = `http://192.168.0.105:5000/api/product/read/${id}`;
      const url = `http://localhost:1000/api/product/get_product/${id}`;

      axios.get(url)
        .then(response => {
          console.log(response.data);
          this.selectedProduct._id = response.data.data._id;
          this.selectedProduct.sku = response.data.data.sku;
          this.selectedProduct.title = response.data.data.title;
          this.selectedProduct.description = response.data.data.description;
          this.selectedProduct.type = response.data.data.type;
          this.selectedProduct.price = response.data.data.price;

          this.showGetModal = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getProductByIdOnlyData: function(data) {
      let id = data.target.value;
      this.loading = true;

      // const url = `http://192.168.0.105:5000/api/product/read/${id}`;
      const url = `http://localhost:1000/api/product/get_product/${id}`;

      axios.get(url)
        .then(response => {
          this.selectedProduct._id = response.data.data._id;
          this.selectedProduct.sku = response.data.data.sku;
          this.selectedProduct.title = response.data.data.title;
          this.selectedProduct.description = response.data.data.description;
          this.selectedProduct.type = response.data.data.type;
          this.selectedProduct.price = response.data.data.price;

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateProductById: function(data) {
      let id = data.target.value;

      // const url = `http://192.168.0.105:5000/api/product/update/${id}`;
      const url = `http://localhost:1000/api/product/update_product/${id}`;

      console.log(this.selectedProduct)

      axios.put(url, this.selectedProduct)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllProducts();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteProductById: function(data) {
      let id = data.target.value;

      // const url = `http://192.168.0.105:5000/api/product/delete/${id}`;
      const url = `http://localhost:1000/api/product/delete_product/${id}`;

      axios.delete(url)
        .then(response => {

          this.getAllProducts();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    axios.get(`http://localhost:1000/api/product/get_products`)
      .then(response => {
        this.products = response.data.data;

        this.loading = false;
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Products</span>
          <button v-on:click="showPostModal = true; formAction = 'Create'" type="button" class="btn yellow_button">Create</button>
          <button v-on:click="getAllProducts" type="button" class="btn purple_button">Reload</button>
        </h1>
      </div>
      <!-- <div class="row"> -->
        <!-- <p v-if="showSuccessText === true"></p> -->
        <p v-if="showSuccessText === true" class="success_text">Success: some text for success action</p>
        <p v-if="showErrorText === true" class="error_text">Error: some text for error action</p>
        <p v-if="showWarningText === true" class="warning_text">Warning: some text for warning action</p>
      <!-- </div> -->
    </div>

    <div v-if="loading === false" class="products_body table-responsive">
      <table class="table table-sm table-bordered table-hover">
        <thead>
          <tr>
            <th>SKU</th>
            <th>Title</th>
            <th>Description</th>
            <th>Type</th>
            <th>Price</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="product in products">
            <td>{{ product.sku }}</td>
            <td>{{ product.title }}</td>
            <td>{{ product.description }}</td>
            <td>{{ product.type }}</td>
            <td>{{ product.price }}</td>
            <td>
              <button v-bind:value="product._id" v-on:click="getProductById" type="button" class="btn blue_button">View</button>
              <button v-bind:value="product._id" v-on:click="showPostModal = true; formAction = 'Update'; getProductByIdOnlyData($event, product._id)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="product._id" v-on:click="deleteProductById" type="button" class="btn red_button">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>



    <div v-if="showPostModal">
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">{{ formAction }} Product</h5>
                  <!-- <h6 class="error_text">Error: some text for error action</h6> -->
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Update'">Id: <span>{{ selectedProduct._id }}</span></p>
                  <div class="form-group">
                    <label for="productInputName">SKU</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputName" v-model="newProduct.sku">
                    <input v-else type="text" class="form-control" id="productInputName" v-model="selectedProduct.sku" value="selectedProduct.sku">
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Title</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputDescription" v-model="newProduct.title">
                    <input v-else type="text" class="form-control" id="productInputDescription" v-model="selectedProduct.title" value="selectedProduct.title">
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Description</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputDescription" v-model="newProduct.description">
                    <input v-else type="text" class="form-control" id="productInputDescription" v-model="selectedProduct.description" value="selectedProduct.description">
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Type</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputDescription" v-model="newProduct.type">
                    <input v-else type="text" class="form-control" id="productInputDescription" v-model="selectedProduct.type" value="selectedProduct.type">
                  </div>

                  <div class="form-group">
                    <label for="productInputPrice">Price</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputPrice" v-model="newProduct.price">
                    <input v-else type="text" class="form-control" id="productInputPrice" v-model="selectedProduct.price" value="selectedProduct.price">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Close</button>
                  <button v-if="formAction === 'Create'" type="button" class="btn yellow_button" @click.prevent="createProduct()">{{ formAction }}</button>
                  <button v-else type="button" class="btn green_button" v-bind:value="selectedProduct._id" @click.prevent="updateProductById">{{ formAction }}</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>



    <div v-if="showGetModal">
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Product View</h5>
                </div>
                <div class="modal-body">
                  <p>SKU: <span>{{ selectedProduct.sku }}</span></p>
                  <p>Title: <span>{{ selectedProduct.title }}</span></p>
                  <p>Description: <span>{{ selectedProduct.description }}</span></p>
                  <p>Type: <span>{{ selectedProduct.type }}</span></p>
                  <p>Price: <span>{{ selectedProduct.price }}</span></p>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showGetModal = false">Close</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>



    <div v-if="loading === true" class="spring-spinner">
      <div class="spring-spinner-part top">
        <div class="spring-spinner-rotator"></div>
      </div>
      <div class="spring-spinner-part bottom">
        <div class="spring-spinner-rotator"></div>
      </div>
    </div>

  </div>
  `
}
