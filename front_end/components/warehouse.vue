const Warehouse  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      classifiers: [],
      warehouses: [],
      showGetModal: false,
      showPostModal: false,
      formAction: '',
      selectedWarehouse: {
        id_wh: null,
        code: null,
        supplier: '',
        receipt_date: null,
        year: null,
        month: null,
        day: null,
        value_product: null,
        price: null,
        first_value: null
      },
      newWarehouse: {
        code: null,
        supplier: '',
        receipt_date: null,
        year: null,
        month: null,
        day: null,
        value_product: null,
        price: null,
        first_value: null
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

    getAllClassifiers: function() {
      const url = 'http://192.168.0.105:5000/api/classifier/read_all'

      axios.get(url)
        .then(response => {
          this.classifiers = response.data.data
          console.log(this.classifiers);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    createWarehouse: function() {
      const url = 'http://192.168.0.105:5000/api/warehouse/create';

      this.newWarehouse.receipt_date = `${this.newWarehouse.year}${this.newWarehouse.month}${this.newWarehouse.day}`

      axios.post(url, this.newWarehouse)
        .then(response => {

          console.log(this.newWarehouse)

          console.log(response);

          this.showPostModal = false;
          this.getAllWarehouses();
          this.showActionText('success');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllWarehouses: function() {
      const url = 'http://192.168.0.105:5000/api/warehouse/read_all'

      this.loading = true;

      axios.get(url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.warehouses = response.data.data;
          } else {
            console.log('object');
            this.warehouses = [response.data.data];
          }

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getWarehouseById: function(data) {
      let id_wh = data.target.value;

      const url = `http://192.168.0.105:5000/api/warehouse/read/${id_wh}`;

      axios.get(url)
        .then(response => {
          this.selectedWarehouse.id_wh = response.data.data.id_wh;
          this.selectedWarehouse.code = response.data.data.code;
          this.selectedWarehouse.supplier = response.data.data.supplier;
          this.selectedWarehouse.receipt_date = response.data.data.receipt_date;
          this.selectedWarehouse.value_product = response.data.data.value_product;
          this.selectedWarehouse.price = response.data.data.price;
          this.selectedWarehouse.first_value = response.data.data.first_value;

          this.showGetModal = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getWarehouseByIdOnlyData: function(data) {
      let id_wh = data.target.value;
      this.loading = true;

      const url = `http://192.168.0.105:5000/api/warehouse/read/${id_wh}`;

      axios.get(url)
        .then(response => {
          this.selectedWarehouse.id_wh = response.data.data.id_wh;
          this.selectedWarehouse.code = response.data.data.code;
          this.selectedWarehouse.supplier = response.data.data.supplier;
          this.selectedWarehouse.receipt_date = response.data.data.receipt_date.split('-');
          this.selectedWarehouse.value_product = response.data.data.value_product;
          this.selectedWarehouse.price = response.data.data.price;
          this.selectedWarehouse.first_value = response.data.data.first_value;


          this.selectedWarehouse.month = this.selectedWarehouse.receipt_date[1];
          this.selectedWarehouse.day = this.selectedWarehouse.receipt_date[2];
          this.selectedWarehouse.year = this.selectedWarehouse.receipt_date[0];

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateWarehouseById: function(data) {
      let id_wh = data.target.value;

      const url = `http://192.168.0.105:5000/api/warehouse/update/${id_wh}`;

      this.selectedWarehouse.receipt_date = `${this.selectedWarehouse.year}${this.selectedWarehouse.month}${this.selectedWarehouse.day}`

      console.log(this.selectedWarehouse)

      axios.put(url, this.selectedWarehouse)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllWarehouses();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteWarehouseById: function(data) {
      let id_wh = data.target.value;

      const url = `http://192.168.0.105:5000/api/warehouse/delete/${id_wh}`;

      axios.delete(url)
        .then(response => {

          this.getAllWarehouses();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    axios.get(`http://192.168.0.105:5000/api/warehouse/read_all`)
      .then(response => {
        if (Array.isArray(response.data.data)) {
          console.log('array');
          this.warehouses = response.data.data;
        } else {
          console.log('object');
          this.warehouses = [response.data.data];
        }

        this.loading = false;
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Warehouse</span>
          <button v-on:click="showPostModal = true; formAction = 'Create'; getAllClassifiers()" type="button" class="btn yellow_button">Create</button>
          <button v-on:click="getAllWarehouses" type="button" class="btn purple_button">Reload</button>
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
            <th>Classifier Code</th>
            <th>Supplier</th>
            <th>Receipt Date</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="warehouse in warehouses">
            <td>{{ warehouse.code }}</td>
            <td>{{ warehouse.supplier }}</td>
            <td>{{ warehouse.receipt_date }}</td>
            <td>
              <button v-bind:value="warehouse.id_wh" v-on:click="getWarehouseById" type="button" class="btn blue_button">View</button>
              <button v-bind:value="warehouse.id_wh" v-on:click="showPostModal = true; formAction = 'Update'; getWarehouseByIdOnlyData($event, warehouse.id_wh)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="warehouse.id_wh" v-on:click="deleteWarehouseById" type="button" class="btn red_button">Delete</button>
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
                  <h5 class="modal-title">{{ formAction }} Warehouse</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Update'">Id: <span>{{ selectedWarehouse.id_wh }}</span></p>

                  <div v-if="formAction === 'Create'" class="form-group">
                    <label for="warehouseInputName">Classifier Code</label>
                    <select v-model="newWarehouse.code" class="form-control" id="warehouseInputCode">
                      <option v-for="classifier in classifiers">{{ classifier.code }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Classifier Code: <span>{{ selectedWarehouse.code }}</span></p>
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputDescription">Supplier</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="warehouseInputSupplier" v-model="newWarehouse.supplier">
                    <input v-else type="text" class="form-control" id="warehouseInputSupplier" v-model="selectedWarehouse.supplier" value="selectedWarehouse.supplier">
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputDescription">Receipt Date</label>
                    <!-- <input v-if="formAction === 'Create'" type="text" class="form-control" id="warehouseInputDate" v-model="newWarehouse.receipt_date"> -->
                    <!-- <input v-else type="text" class="form-control" id="warehouseInputDate" v-model="selectedWarehouse.receipt_date" value="selectedWarehouse.receipt_date"> -->

                    <div class="row">
                      <div class="col">
                        <input v-if="formAction === 'Create'" v-model="newWarehouse.month" type="text" class="form-control" placeholder="Month(MM)">
                        <input v-else type="text" v-model="selectedWarehouse.month" value="selectedWarehouse.month" class="form-control" placeholder="Month(MM)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Create'" v-model="newWarehouse.day" type="text" class="form-control" placeholder="Day(DD)">
                        <input v-else type="text" v-model="selectedWarehouse.day" value="selectedWarehouse.day" class="form-control" placeholder="Day(DD)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Create'" v-model="newWarehouse.year" type="text" class="form-control" placeholder="Year(YYYY)">
                        <input v-else type="text" v-model="selectedWarehouse.year" value="selectedWarehouse.year" class="form-control" placeholder="Year(YYYY)">
                      </div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputDescription">Product Value</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="warehouseInputProductValue" v-model="newWarehouse.value_product">
                    <input v-else type="text" class="form-control" id="warehouseInputProductValue" v-model="selectedWarehouse.value_product" value="selectedWarehouse.value_product">
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputPrice">Price</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="warehouseInputPrice" v-model="newWarehouse.price">
                    <input v-else type="text" class="form-control" id="warehouseInputPrice" v-model="selectedWarehouse.price" value="selectedWarehouse.price">
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputPrice">First Value</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="warehouseFirstValue" v-model="newWarehouse.first_value">
                    <input v-else type="text" class="form-control" id="warehouseFirstValue" v-model="selectedWarehouse.first_value" value="selectedWarehouse.first_value">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Close</button>
                  <button v-if="formAction === 'Create'" type="button" class="btn yellow_button" @click.prevent="createWarehouse()">{{ formAction }}</button>
                  <button v-else type="button" class="btn green_button" v-bind:value="selectedWarehouse.id_wh" @click.prevent="updateWarehouseById">{{ formAction }}</button>
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
                  <p>Warehouse Id: <span>{{ selectedWarehouse.id_wh }}</span></p>
                  <p>Classifier Code: <span>{{ selectedWarehouse.code }}</span></p>
                  <p>Supplier: <span>{{ selectedWarehouse.supplier }}</span></p>
                  <p>Receipt Date: <span>{{ selectedWarehouse.receipt_date }}</span></p>
                  <p>Product Value: <span>{{ selectedWarehouse.value_product }}</span></p>
                  <p>Price: <span>{{ selectedWarehouse.price }}</span></p>
                  <p>First Value: <span>{{ selectedWarehouse.first_value }}</span></p>
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
