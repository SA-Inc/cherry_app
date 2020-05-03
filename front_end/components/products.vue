const Product  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      classifiers: [],
      warehouses: [],
      sellers: [],
      products: [],
      showGetModal: false,
      showPostModal: false,
      formAction: '',
      selectedProduct: {
        id_prod: null,
        value_product: null,
        date_sell: null,
        year: null,
        month: null,
        day: null,
        price_prod: null,
        id_sell: null,
        id_wh: null,
        code: null
      },
      newProduct: {
        value_product: null,
        date_sell: null,
        year: null,
        month: null,
        day: null,
        price_prod: null,
        id_sell: null,
        id_wh: null,
        code: null
      },
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

    getAllClassifiersWarehousesIdsAndSellerIds: async function() {
      const classifier_url = 'http://192.168.0.105:5000/api/classifier/read_all'
      const warehouse_url = 'http://192.168.0.105:5000/api/warehouse/read_ids'
      const seller_url = 'http://192.168.0.105:5000/api/seller/read_ids'

      await axios.get(classifier_url)
        .then(response => {
          this.classifiers = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });

      await axios.get(warehouse_url)
        .then(response => {
          this.warehouses = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });

      await axios.get(seller_url)
        .then(response => {
          this.sellers = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    createProduct: function() {
      const url = 'http://192.168.0.105:5000/api/product/create';

      this.newProduct.date_sell = `${this.newProduct.year}${this.newProduct.month}${this.newProduct.day}`

      axios.post(url, this.newProduct)
        .then(response => {

          console.log(this.newProduct)

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
      const url = 'http://192.168.0.105:5000/api/product/read_all'

      this.loading = true;

      axios.get(url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.products = response.data.data;
          } else {
            console.log('object');
            this.products = [response.data.data];
          }

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getProductById: function(data) {
      let id_prod = data.target.value;

      const url = `http://192.168.0.105:5000/api/product/read/${id_prod}`;

      axios.get(url)
        .then(response => {
          this.selectedProduct.id_prod = response.data.data.id_prod;
          this.selectedProduct.value_product = response.data.data.value_product;
          this.selectedProduct.date_sell = response.data.data.date_sell;
          this.selectedProduct.price_prod = response.data.data.price_prod;
          this.selectedProduct.id_sell = response.data.data.id_sell;
          this.selectedProduct.id_wh = response.data.data.id_wh;
          this.selectedProduct.code = response.data.data.code;

          this.showGetModal = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getProductByIdOnlyData: function(data) {
      let id_prod = data.target.value;
      this.loading = true;

      const url = `http://192.168.0.105:5000/api/product/read/${id_prod}`;

      axios.get(url)
        .then(response => {
          this.selectedProduct.id_prod = response.data.data.id_prod;
          this.selectedProduct.value_product = response.data.data.value_product;
          this.selectedProduct.date_sell = response.data.data.date_sell.split('-');
          this.selectedProduct.price_prod = response.data.data.price_prod;
          this.selectedProduct.id_sell = response.data.data.id_sell;
          this.selectedProduct.id_wh = response.data.data.id_wh;
          this.selectedProduct.code = response.data.data.code;


          this.selectedProduct.month = this.selectedProduct.date_sell[1];
          this.selectedProduct.day = this.selectedProduct.date_sell[2];
          this.selectedProduct.year = this.selectedProduct.date_sell[0];

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateProductById: function(data) {
      let id_prod = data.target.value;

      const url = `http://192.168.0.105:5000/api/product/update/${id_prod}`;

      this.selectedProduct.date_sell = `${this.selectedProduct.year}${this.selectedProduct.month}${this.selectedProduct.day}`

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
      let id_prod = data.target.value;

      const url = `http://192.168.0.105:5000/api/product/delete/${id_prod}`;

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
    axios.get(`http://192.168.0.105:5000/api/product/read_all`)
      .then(response => {
        if (Array.isArray(response.data.data)) {
          console.log('array');
          this.products = response.data.data;
        } else {
          console.log('object');
          this.products = [response.data.data];
        }

        this.loading = false;
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Product</span>
          <button v-on:click="showPostModal = true; formAction = 'Create'; getAllClassifiersWarehousesIdsAndSellerIds()" type="button" class="btn yellow_button">Create</button>
          <button v-on:click="getAllProducts" type="button" class="btn purple_button">Reload</button>
        </h1>
      </div>
        <p v-if="showSuccessText === true" class="success_text">Success: some text for success action</p>
        <p v-if="showErrorText === true" class="error_text">Error: some text for error action</p>
        <p v-if="showWarningText === true" class="warning_text">Warning: some text for warning action</p>
    </div>

    <div v-if="loading === false" class="table-responsive">
      <table class="table table-sm table-bordered table-hover">
        <thead>
          <tr>
            <th>Product Value</th>
            <th>Sell Date</th>
            <th>Price</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="product in products">
            <td>{{ product.value_product }}</td>
            <td>{{ product.date_sell }}</td>
            <td>{{ product.price_prod }}</td>
            <td>
              <button v-bind:value="product.id_prod" v-on:click="getProductById" type="button" class="btn blue_button">View</button>
              <button v-bind:value="product.id_prod" v-on:click="showPostModal = true; formAction = 'Update'; getProductByIdOnlyData($event, product.id_prod)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="product.id_prod" v-on:click="deleteProductById" type="button" class="btn red_button">Delete</button>
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
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Update'">Id: <span>{{ selectedProduct.id_prod }}</span></p>

                  <div v-if="formAction === 'Create'" class="form-group">
                    <label for="productInputName">Warehouse Id</label>
                    <select v-model="newProduct.id_wh" class="form-control" id="productInputCode">
                      <option v-for="warehouse in warehouses">{{ warehouse.id_wh }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Warehouse Id: <span>{{ selectedProduct.id_wh }}</span></p>
                  </div>

                  <div v-if="formAction === 'Create'" class="form-group">
                    <label for="productInputName">Seller Id</label>
                    <select v-model="newProduct.id_sell" class="form-control" id="productInputCode">
                      <option v-for="seller in sellers">{{ seller.id_sell }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Seller Id: <span>{{ selectedProduct.id_sell }}</span></p>
                  </div>

                  <div v-if="formAction === 'Create'" class="form-group">
                    <label for="productInputName">Classifier Code</label>
                    <select v-model="newProduct.code" class="form-control" id="productInputCode">
                      <option v-for="classifier in classifiers">{{ classifier.code }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Classifier Code: <span>{{ selectedProduct.code }}</span></p>
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Receipt Date</label>
                    <div class="row">
                      <div class="col">
                        <input v-if="formAction === 'Create'" v-model="newProduct.month" type="text" class="form-control" placeholder="Month(MM)">
                        <input v-else type="text" v-model="selectedProduct.month" value="selectedProduct.month" class="form-control" placeholder="Month(MM)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Create'" v-model="newProduct.day" type="text" class="form-control" placeholder="Day(DD)">
                        <input v-else type="text" v-model="selectedProduct.day" value="selectedProduct.day" class="form-control" placeholder="Day(DD)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Create'" v-model="newProduct.year" type="text" class="form-control" placeholder="Year(YYYY)">
                        <input v-else type="text" v-model="selectedProduct.year" value="selectedProduct.year" class="form-control" placeholder="Year(YYYY)">
                      </div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Product Value</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputProductValue" v-model="newProduct.value_product">
                    <input v-else type="text" class="form-control" id="productInputProductValue" v-model="selectedProduct.value_product" value="selectedProduct.value_product">
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Product Price</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="productInputProductValue" v-model="newProduct.price_prod">
                    <input v-else type="text" class="form-control" id="productInputProductValue" v-model="selectedProduct.price_prod" value="selectedProduct.price_prod">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Close</button>
                  <button v-if="formAction === 'Create'" type="button" class="btn yellow_button" @click.prevent="createProduct()">{{ formAction }}</button>
                  <button v-else type="button" class="btn green_button" v-bind:value="selectedProduct.id_prod" @click.prevent="updateProductById">{{ formAction }}</button>
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
                  <p>Product Id: <span>{{ selectedProduct.id_prod }}</span></p>
                  <p>Warehouse Id: <span>{{ selectedProduct.id_wh }}</span></p>
                  <p>Seller Id: <span>{{ selectedProduct.id_sell }}</span></p>
                  <p>Classifier Code: <span>{{ selectedProduct.code }}</span></p>
                  <p>Sell Date Value: <span>{{ selectedProduct.date_sell }}</span></p>
                  <p>Product Value: <span>{{ selectedProduct.value_product }}</span></p>
                  <p>Price: <span>{{ selectedProduct.price_prod }}</span></p>
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
