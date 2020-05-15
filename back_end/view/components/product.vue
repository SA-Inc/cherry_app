const Product  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      success_message: '',
      error_message: '',
      warning_message: '',
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
    showActionText: function(action, message) {
      if (action === 'success') {
        this.showSuccessText = true;
        this.success_message = message;

        setTimeout(function() {
          this.showSuccessText = false;
        }.bind(this), 2000);
      }

      if (action === 'error') {
        this.showErrorText = true;
        this.error_message = message;

        setTimeout(function() {
          this.showErrorText = false;
        }.bind(this), 2000);
      }

      if (action === 'warning') {
        this.showWarningText = true;
        this.warning_message = message;

        setTimeout(function() {
          this.showWarningText = false;
        }.bind(this), 2000);
      }
    },

    getAllClassifiersWarehousesIdsAndSellerIds: async function() {
      const classifier_url = '/api/classifier/read_all'
      const warehouse_url = '/api/warehouse/read_ids'
      const seller_url = '/api/seller/read_ids'

      await axios.get(classifier_url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.classifiers = response.data.data;
          } else {
            console.log('object');
            this.classifiers = [response.data.data];
          }
        })
        .catch((error) => {
          console.log(error);
        });

      await axios.get(warehouse_url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.warehouses = response.data.data;
          } else {
            console.log('object');
            this.warehouses = [response.data.data];
          }
        })
        .catch((error) => {
          console.log(error);
        });

      await axios.get(seller_url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.sellers = response.data.data;
          } else {
            console.log('object');
            this.sellers = [response.data.data];
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    createProduct: function() {
      const url = '/api/product/create';

      this.newProduct.date_sell = `${this.newProduct.year}${this.newProduct.month}${this.newProduct.day}`

      axios.post(url, this.newProduct)
        .then(response => {

          console.log(this.newProduct)

          console.log(response);

          this.showPostModal = false;
          this.getAllProducts();
          this.showActionText('success', 'Product was created');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllProducts: function() {
      const url = '/api/product/read_all'

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
          // if (error.response.status === 404) {
          //   this.loading = false;
          //   this.showActionText('error', 'Products not found');
          // }
        });
    },

    getProductById: function(data) {
      let id_prod = data.target.value;

      const url = `/api/product/read/${id_prod}`;

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

      const url = `/api/product/read/${id_prod}`;

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

      const url = `/api/product/update/${id_prod}`;

      this.selectedProduct.date_sell = `${this.selectedProduct.year}${this.selectedProduct.month}${this.selectedProduct.day}`

      console.log(this.selectedProduct)

      axios.put(url, this.selectedProduct)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllProducts();
          this.showActionText('success', 'Product was updated');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteProductById: function(data) {
      let id_prod = data.target.value;

      const url = `/api/product/delete/${id_prod}`;

      axios.delete(url)
        .then(response => {

          this.getAllProducts();
          this.showActionText('success', 'Product was deleted');
        })
        .catch((error) => {
          if (error.response.data.code === 23000) {
            this.showActionText('error', 'Can not Delete Row. Foreign Key Reference Constraint');
          }
        });
    },
  },
  mounted() {
    axios.get(`/api/product/read_all`)
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
        if (error.response.status === 404) {
          this.loading = false;
          this.showActionText('error', 'Products not found');
        }
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <!-- <span>Product</span> -->
          <span>Товары</span>
          <!-- <button v-on:click="showPostModal = true; formAction = 'Create'; getAllClassifiersWarehousesIdsAndSellerIds()" type="button" class="btn yellow_button">Create</button> -->
          <button v-on:click="showPostModal = true; formAction = 'Создать'; getAllClassifiersWarehousesIdsAndSellerIds()" type="button" class="btn yellow_button">Создать</button>
          <!-- <button v-on:click="getAllProducts" type="button" class="btn purple_button">Reload</button> -->
          <button v-on:click="getAllProducts" type="button" class="btn purple_button">Обновить</button>
        </h1>
      </div>
        <p v-if="showSuccessText === true" class="success_text">Success: {{ success_message }}</p>
        <p v-if="showErrorText === true" class="error_text">Error: {{ error_message }}</p>
        <p v-if="showWarningText === true" class="warning_text">Warning: {{ warning_message }}</p>
    </div>

    <div v-if="loading === false" class="table-responsive">
      <table class="table table-sm table-bordered table-hover">
        <thead>
          <tr>
            <!-- <th>Product Value</th>
            <th>Sell Date</th>
            <th>Price</th>
            <th>Actions</th> -->
            <th>Объем продажи</th>
            <th>Дата продажи</th>
            <th>Цена</th>
            <th>Действия</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="product in products">
            <td>{{ product.value_product }}</td>
            <td>{{ product.date_sell }}</td>
            <td>{{ product.price_prod }}</td>
            <td>
              <!-- <button v-bind:value="product.id_prod" v-on:click="getProductById" type="button" class="btn blue_button">View</button> -->
              <button v-bind:value="product.id_prod" v-on:click="getProductById" type="button" class="btn blue_button">Посмотреть</button>
              <!-- <button v-bind:value="product.id_prod" v-on:click="showPostModal = true; formAction = 'Update'; getProductByIdOnlyData($event, product.id_prod)" type="button" class="btn green_button">Edit</button> -->
              <button v-bind:value="product.id_prod" v-on:click="showPostModal = true; formAction = 'Редактировать'; getProductByIdOnlyData($event, product.id_prod)" type="button" class="btn green_button">Редактировать</button>
              <!-- <button v-bind:value="product.id_prod" v-on:click="deleteProductById" type="button" class="btn red_button">Delete</button> -->
              <button v-bind:value="product.id_prod" v-on:click="deleteProductById" type="button" class="btn red_button">Удалить</button>
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
                  <h5 class="modal-title">{{ formAction }} товар</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Редактировать'">Id: <span>{{ selectedProduct.id_prod }}</span></p>

                  <div v-if="formAction === 'Создать'" class="form-group">
                    <label for="productInputName">Id Склада</label>
                    <select v-model="newProduct.id_wh" class="form-control" id="productInputCode">
                      <option v-for="warehouse in warehouses">{{ warehouse.id_wh }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Id Склада: <span>{{ selectedProduct.id_wh }}</span></p>
                  </div>

                  <div v-if="formAction === 'Создать'" class="form-group">
                    <label for="productInputName">Id Продавца</label>
                    <select v-model="newProduct.id_sell" class="form-control" id="productInputCode">
                      <option v-for="seller in sellers">{{ seller.id_sell }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Id Продавца: <span>{{ selectedProduct.id_sell }}</span></p>
                  </div>

                  <div v-if="formAction === 'Создать'" class="form-group">
                    <label for="productInputName">Код классификатора</label>
                    <select v-model="newProduct.code" class="form-control" id="productInputCode">
                      <option v-for="classifier in classifiers">{{ classifier.code }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Код классификатора: <span>{{ selectedProduct.code }}</span></p>
                  </div>

                  <div class="form-group">
                    <!-- <label for="productInputDescription">Receipt Date</label> -->
                    <label for="productInputDescription">Дата продажи</label>
                    <div class="row">
                      <div class="col">
                        <input v-if="formAction === 'Создать'" v-model="newProduct.month" type="text" class="form-control" placeholder="Месяц(MM)">
                        <input v-else type="text" v-model="selectedProduct.month" value="selectedProduct.month" class="form-control" placeholder="Месяц(MM)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Создать'" v-model="newProduct.day" type="text" class="form-control" placeholder="День(DD)">
                        <input v-else type="text" v-model="selectedProduct.day" value="selectedProduct.day" class="form-control" placeholder="День(DD)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Создать'" v-model="newProduct.year" type="text" class="form-control" placeholder="Год(YYYY)">
                        <input v-else type="text" v-model="selectedProduct.year" value="selectedProduct.year" class="form-control" placeholder="Год(YYYY)">
                      </div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Объем продажи</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="productInputProductValue" v-model="newProduct.value_product">
                    <input v-else type="text" class="form-control" id="productInputProductValue" v-model="selectedProduct.value_product" value="selectedProduct.value_product">
                  </div>

                  <div class="form-group">
                    <label for="productInputDescription">Цена</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="productInputProductValue" v-model="newProduct.price_prod">
                    <input v-else type="text" class="form-control" id="productInputProductValue" v-model="selectedProduct.price_prod" value="selectedProduct.price_prod">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Закрыть</button>
                  <button v-if="formAction === 'Создать'" type="button" class="btn yellow_button" @click.prevent="createProduct()">{{ formAction }}</button>
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
                  <h5 class="modal-title">Просмотр товара</h5>
                </div>
                <div class="modal-body">
                  <p>Id Товара: <span>{{ selectedProduct.id_prod }}</span></p>
                  <p>Id Склада: <span>{{ selectedProduct.id_wh }}</span></p>
                  <p>Id Продавца: <span>{{ selectedProduct.id_sell }}</span></p>
                  <p>Код классификатора: <span>{{ selectedProduct.code }}</span></p>
                  <p>Дата продажи: <span>{{ selectedProduct.date_sell }}</span></p>
                  <p>Объем продажи: <span>{{ selectedProduct.value_product }}</span></p>
                  <p>Цена: <span>{{ selectedProduct.price_prod }}</span></p>
                  <!-- <p>Product Id: <span>{{ selectedProduct.id_prod }}</span></p>
                  <p>Warehouse Id: <span>{{ selectedProduct.id_wh }}</span></p>
                  <p>Seller Id: <span>{{ selectedProduct.id_sell }}</span></p>
                  <p>Classifier Code: <span>{{ selectedProduct.code }}</span></p>
                  <p>Sell Date Value: <span>{{ selectedProduct.date_sell }}</span></p>
                  <p>Product Value: <span>{{ selectedProduct.value_product }}</span></p>
                  <p>Price: <span>{{ selectedProduct.price_prod }}</span></p> -->
                </div>
                <div class="modal-footer">
                  <!-- <button type="button" class="btn red_button" v-on:click="showGetModal = false">Close</button> -->
                  <button type="button" class="btn red_button" v-on:click="showGetModal = false">Закрыть</button>
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
