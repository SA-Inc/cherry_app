const Supplier  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      success_message: '',
      error_message: '',
      warning_message: '',
      suppliers: [],
      showGetModal: false,
      showPostModal: false,
      formAction: '',
      warehouses: [],
      selectedSupplier: {
        id_sup: null,
        company_name: '',
        bank: '',
        account_number: '',
        phone_number: '',
        email: '',
        id_wh: null
      },
      newSupplier: {
        company_name: '',
        bank: '',
        account_number: '',
        phone_number: '',
        email: '',
        id_wh: null
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

    getAllWarehousesId: function() {
      const url = '/api/warehouse/read_ids'

      axios.get(url)
        .then(response => {
          this.warehouses = response.data.data
          console.log(this.warehouses);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    createSupplier: function() {
      const url = '/api/supplier/create';

      axios.post(url, this.newSupplier)
        .then(response => {

          console.log(this.newSupplier)

          console.log(response);

          this.showPostModal = false;
          this.getAllSuppliers();
          this.showActionText('success', 'Supplier was created');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllSuppliers: function() {
      const url = '/api/supplier/read_all'

      this.loading = true;

      axios.get(url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.suppliers = response.data.data;
          } else {
            console.log('object');
            this.suppliers = [response.data.data];
          }

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getSupplierById: function(data) {
      let id_sup = data.target.value;

      const url = `/api/supplier/read/${id_sup}`;

      axios.get(url)
        .then(response => {
          this.selectedSupplier.id_sup = response.data.data.id_sup;
          this.selectedSupplier.company_name = response.data.data.company_name;
          this.selectedSupplier.bank = response.data.data.bank;
          this.selectedSupplier.account_number = response.data.data.account_number;
          this.selectedSupplier.phone_number = response.data.data.phone_number;
          this.selectedSupplier.email = response.data.data.email;
          this.selectedSupplier.id_wh = response.data.data.id_wh;

          this.showGetModal = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getSupplierByIdOnlyData: function(data) {
      let id_sup = data.target.value;
      this.loading = true;

      const url = `/api/supplier/read/${id_sup}`;

      axios.get(url)
        .then(response => {
          this.selectedSupplier.id_sup = response.data.data.id_sup;
          this.selectedSupplier.company_name = response.data.data.company_name;
          this.selectedSupplier.bank = response.data.data.bank;
          this.selectedSupplier.account_number = response.data.data.account_number;
          this.selectedSupplier.phone_number = response.data.data.phone_number;
          this.selectedSupplier.email = response.data.data.email;
          this.selectedSupplier.id_wh = response.data.data.id_wh;

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateSupplierById: function(data) {
      let id_sup = data.target.value;

      const url = `/api/supplier/update/${id_sup}`;

      console.log(this.selectedSupplier)

      axios.put(url, this.selectedSupplier)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllSuppliers();
          this.showActionText('success', 'Supplier was updated');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteSupplierById: function(data) {
      let id_sup = data.target.value;

      const url = `/api/supplier/delete/${id_sup}`;

      axios.delete(url)
        .then(response => {

          this.getAllSuppliers();
          this.showActionText('success', 'Supplier was deleted');
        })
        .catch((error) => {
          if (error.response.data.code === 23000) {
            this.showActionText('error', 'Can not Delete Row. Foreign Key Reference Constraint');
          }
        });
    },
  },
  mounted() {
    axios.get(`/api/supplier/read_all`)
      .then(response => {
        if (Array.isArray(response.data.data)) {
          console.log('array');
          this.suppliers = response.data.data;
        } else {
          console.log('object');
          this.suppliers = [response.data.data];
        }

        this.loading = false;
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Supplier</span>
          <button v-on:click="showPostModal = true; formAction = 'Create'; getAllWarehousesId()" type="button" class="btn yellow_button">Create</button>
          <button v-on:click="getAllSuppliers" type="button" class="btn purple_button">Reload</button>
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
            <th>Account Number</th>
            <th>Company Name</th>
            <th>Phone Number</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="supplier in suppliers">
            <td>{{ supplier.account_number }}</td>
            <td>{{ supplier.company_name }}</td>
            <td>{{ supplier.phone_number }}</td>
            <td>
              <button v-bind:value="supplier.id_sup" v-on:click="getSupplierById" type="button" class="btn blue_button">View</button>
              <button v-bind:value="supplier.id_sup" v-on:click="showPostModal = true; formAction = 'Update'; getSupplierByIdOnlyData($event, supplier.id_sup)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="supplier.id_sup" v-on:click="deleteSupplierById" type="button" class="btn red_button">Delete</button>
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
                  <h5 class="modal-title">{{ formAction }} Supplier</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Update'">Id: <span>{{ selectedSupplier.id_sup }}</span></p>

                  <div v-if="formAction === 'Create'" class="form-group">
                    <label for="supplierInputWarehouseId">Warehouse Id</label>
                    <select v-model="newSupplier.id_wh" class="form-control" id="supplierInputWarehouseId">
                      <option v-for="warehouse in warehouses">{{ warehouse.id_wh }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Warehouse Id: <span>{{ selectedSupplier.id_wh }}</span></p>
                  </div>

                  <div class="form-group">
                    <label for="supplierInputCompanyName">Company Name</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="supplierInputCompanyName" v-model="newSupplier.company_name">
                    <input v-else type="text" class="form-control" id="supplierInputCompanyName" v-model="selectedSupplier.company_name" value="selectedSupplier.company_name">
                  </div>

                  <div class="form-group">
                    <label for="supplierInputDescription">Bank</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="supplierInputProductValue" v-model="newSupplier.bank">
                    <input v-else type="text" class="form-control" id="supplierInputProductValue" v-model="selectedSupplier.bank" value="selectedSupplier.bank">
                  </div>

                  <div class="form-group">
                    <label for="supplierInputPrice">Account Number</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="supplierInputPrice" v-model="newSupplier.account_number">
                    <input v-else type="text" class="form-control" id="supplierInputPrice" v-model="selectedSupplier.account_number" value="selectedSupplier.account_number">
                  </div>

                  <div class="form-group">
                    <label for="supplierInputPrice">Phone Number</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="supplierFirstValue" v-model="newSupplier.phone_number">
                    <input v-else type="text" class="form-control" id="supplierFirstValue" v-model="selectedSupplier.phone_number" value="selectedSupplier.phone_number">
                  </div>

                  <div class="form-group">
                    <label for="supplierInputPrice">Email</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="supplierFirstValue" v-model="newSupplier.email">
                    <input v-else type="text" class="form-control" id="supplierFirstValue" v-model="selectedSupplier.email" value="selectedSupplier.email">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Close</button>
                  <button v-if="formAction === 'Create'" type="button" class="btn yellow_button" @click.prevent="createSupplier()">{{ formAction }}</button>
                  <button v-else type="button" class="btn green_button" v-bind:value="selectedSupplier.id_sup" @click.prevent="updateSupplierById">{{ formAction }}</button>
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
                  <h5 class="modal-title">Supplier View</h5>
                </div>
                <div class="modal-body">
                  <p>Supplier Id: <span>{{ selectedSupplier.id_sup }}</span></p>
                  <p>Warehouse Id: <span>{{ selectedSupplier.id_wh }}</span></p>
                  <p>Account Number: <span>{{ selectedSupplier.account_number }}</span></p>
                  <p>Bank: <span>{{ selectedSupplier.bank }}</span></p>
                  <p>Company Name: <span>{{ selectedSupplier.company_name }}</span></p>
                  <p>Email: <span>{{ selectedSupplier.email }}</span></p>
                  <p>Phone Number: <span>{{ selectedSupplier.phone_number }}</span></p>
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
