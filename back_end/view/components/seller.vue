const Seller  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      sellers: [],
      showGetModal: false,
      showPostModal: false,
      formAction: '',
      selectedSeller: {
        id_sell: null,
        status: null,
        FIO: '',
        value_product: null
      },
      newSeller: {
        status: false,
        FIO: '',
        value_product: null
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

    createSeller: function() {
      const url = '/api/seller/create';

      axios.post(url, this.newSeller)
        .then(response => {

          console.log(this.newSeller)

          console.log(response);

          this.showPostModal = false;
          this.getAllSellers();
          this.showActionText('success');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllSellers: function() {
      const url = '/api/seller/read_all'

      this.loading = true;

      axios.get(url)
        .then(response => {
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.sellers = response.data.data;
          } else {
            console.log('object');
            this.sellers = [response.data.data];
          }

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getSellerById: function(data) {
      let id_sell = data.target.value;

      const url = `/api/seller/read/${id_sell}`;

      axios.get(url)
        .then(response => {
          this.selectedSeller.id_sell = response.data.data.id_sell;
          this.selectedSeller.FIO = response.data.data.FIO;
          this.selectedSeller.status = response.data.data.status;
          this.selectedSeller.value_product = response.data.data.value_product;

          this.showGetModal = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getSellerByIdOnlyData: function(data) {
      let id_sell = data.target.value;
      this.loading = true;

      const url = `/api/seller/read/${id_sell}`;

      axios.get(url)
        .then(response => {
          this.selectedSeller.id_sell = response.data.data.id_sell;
          this.selectedSeller.FIO = response.data.data.FIO;
          this.selectedSeller.status = response.data.data.status;
          this.selectedSeller.value_product = response.data.data.value_product;

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    updateSellerById: function(data) {
      let id_sell = data.target.value;

      const url = `/api/seller/update/${id_sell}`;

      console.log(this.selectedSeller)

      axios.put(url, this.selectedSeller)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllSellers();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteSellerById: function(data) {
      let id_sell = data.target.value;

      const url = `/api/seller/delete/${id_sell}`;

      axios.delete(url)
        .then(response => {

          this.getAllSellers();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    axios.get(`/api/seller/read_all`)
      .then(response => {
        if (Array.isArray(response.data.data)) {
          console.log('array');
          this.sellers = response.data.data;
        } else {
          console.log('object');
          this.sellers = [response.data.data];
        }

        this.loading = false;
      })
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Seller</span>
          <button v-on:click="showPostModal = true; formAction = 'Create'; getAllWarehousesId()" type="button" class="btn yellow_button">Create</button>
          <button v-on:click="getAllSellers" type="button" class="btn purple_button">Reload</button>
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
            <th>Name</th>
            <th>Product Value</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="seller in sellers">
            <td>{{ seller.FIO }}</td>
            <td>{{ seller.value_product }}</td>
            <td v-if="seller.status === true"><span class="success_text">Active</span></td>
            <td v-if="seller.status === false"><span class="error_text">Inactive</span></td>
            <td>
              <button v-bind:value="seller.id_sell" v-on:click="getSellerById" type="button" class="btn blue_button">View</button>
              <button v-bind:value="seller.id_sell" v-on:click="showPostModal = true; formAction = 'Update'; getSellerByIdOnlyData($event, seller.id_sell)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="seller.id_sell" v-on:click="deleteSellerById" type="button" class="btn red_button">Delete</button>
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
                  <h5 class="modal-title">{{ formAction }} Seller</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Update'">Id: <span>{{ selectedSeller.id_sell }}</span></p>

                  <div class="form-group">
                    <label for="sellerInputCompanyName">Name</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="sellerInputCompanyName" v-model="newSeller.FIO">
                    <input v-else type="text" class="form-control" id="sellerInputCompanyName" v-model="selectedSeller.FIO" value="selectedSeller.FIO">
                  </div>

                  <div class="form-group">
                    <label for="sellerInputDescription">Product Value</label>
                    <input v-if="formAction === 'Create'" type="text" class="form-control" id="sellerInputProductValue" v-model="newSeller.value_product">
                    <input v-else type="text" class="form-control" id="sellerInputProductValue" v-model="selectedSeller.value_product" value="selectedSeller.value_product">
                  </div>

                  <div class="form-group">
                    <div class="form-check">
                      <input v-if="formAction === 'Create'" v-model="newSeller.status" class="form-check-input" type="checkbox" id="ststusCheck">
                      <input v-else v-model="selectedSeller.status" value="selectedSeller.status" class="form-check-input" type="checkbox" id="ststusCheck">
                      <label class="form-check-label" for="ststusCheck">Status</label>
                    </div>
                  </div>

                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Close</button>
                  <button v-if="formAction === 'Create'" type="button" class="btn yellow_button" @click.prevent="createSeller()">{{ formAction }}</button>
                  <button v-else type="button" class="btn green_button" v-bind:value="selectedSeller.id_sell" @click.prevent="updateSellerById">{{ formAction }}</button>
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
                  <h5 class="modal-title">Seller View</h5>
                </div>
                <div class="modal-body">
                  <p>Seller Id: <span>{{ selectedSeller.id_sell }}</span></p>
                  <p>Seller Name: <span>{{ selectedSeller.FIO }}</span></p>
                  <p>Product Value: <span>{{ selectedSeller.value_product }}</span></p>
                  <p v-if="selectedSeller.status === true">Status: <span class="success_text">Active</span></p>
                  <p v-if="selectedSeller.status === false">Status: <span class="error_text">Inactive</span></p>
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
