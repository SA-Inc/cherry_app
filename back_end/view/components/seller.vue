const Seller  = {
  data () {
    return {
      loading: true,
      showSuccessText: false,
      showErrorText: false,
      showWarningText: false,
      success_message: '',
      error_message: '',
      warning_message: '',
      sellers: [],
      showGetModal: false,
      showPostModal: false,
      formAction: '',
      selectedSeller: {
        id_sell: null,
        status_sell: null,
        FIO: '',
        value_product: null
      },
      newSeller: {
        status_sell: false,
        FIO: '',
        value_product: null
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

    createSeller: function() {
      const url = '/api/seller/create';

      axios.post(url, this.newSeller)
        .then(response => {

          console.log(this.newSeller)

          console.log(response);

          this.showPostModal = false;
          this.getAllSellers();
          this.showActionText('success', 'Seller was created');
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
          this.selectedSeller.status_sell = response.data.data.status_sell;
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
          this.selectedSeller.status_sell = response.data.data.status_sell;
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
          this.showActionText('success', 'Seller was updated');
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
          this.showActionText('success', 'Seller was deleted');
        })
        .catch((error) => {
          if (error.response.data.code === 23000) {
            this.showActionText('error', 'Can not Delete Row. Foreign Key Reference Constraint');
          }
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
          <!-- <span>Seller</span> -->
          <span>Продавец</span>
          <!-- <button v-on:click="showPostModal = true; formAction = 'Create'; getAllWarehousesId()" type="button" class="btn yellow_button">Create</button> -->
          <button v-on:click="showPostModal = true; formAction = 'Создать'; getAllWarehousesId()" type="button" class="btn yellow_button">Создать</button>
          <!-- <button v-on:click="getAllSellers" type="button" class="btn purple_button">Reload</button> -->
          <button v-on:click="getAllSellers" type="button" class="btn purple_button">Обновить</button>
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
            <th>Имя</th>
            <th>Объем продажи</th>
            <th>Статус</th>
            <th>Действия</th>
            <!-- <th>Name</th>
            <th>Product Value</th>
            <th>Status</th>
            <th>Actions</th> -->
          </tr>
        </thead>

        <tbody>
          <tr v-for="seller in sellers">
            <td>{{ seller.FIO }}</td>
            <td>{{ seller.value_product }}</td>
            <td v-if="seller.status_sell === true"><span class="success_text">Работает</span></td>
            <td v-if="seller.status_sell === false"><span class="error_text">Уволен</span></td>
            <!-- <td v-if="seller.status_sell === true"><span class="success_text">Active</span></td>
            <td v-if="seller.status_sell === false"><span class="error_text">Inactive</span></td> -->
            <td>
              <button v-bind:value="seller.id_sell" v-on:click="getSellerById" type="button" class="btn blue_button">Посмотреть</button>
              <button v-bind:value="seller.id_sell" v-on:click="showPostModal = true; formAction = 'Редактировать'; getSellerByIdOnlyData($event, seller.id_sell)" type="button" class="btn green_button">Редактировать</button>
              <button v-bind:value="seller.id_sell" v-on:click="deleteSellerById" type="button" class="btn red_button">Удалить</button>
              <!-- <button v-bind:value="seller.id_sell" v-on:click="getSellerById" type="button" class="btn blue_button">View</button>
              <button v-bind:value="seller.id_sell" v-on:click="showPostModal = true; formAction = 'Update'; getSellerByIdOnlyData($event, seller.id_sell)" type="button" class="btn green_button">Edit</button>
              <button v-bind:value="seller.id_sell" v-on:click="deleteSellerById" type="button" class="btn red_button">Delete</button> -->
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
                  <h5 class="modal-title">{{ formAction }} продавца</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Редактировать'">Id: <span>{{ selectedSeller.id_sell }}</span></p>

                  <div class="form-group">
                    <label for="sellerInputCompanyName">Имя</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="sellerInputCompanyName" v-model="newSeller.FIO">
                    <input v-else type="text" class="form-control" id="sellerInputCompanyName" v-model="selectedSeller.FIO" value="selectedSeller.FIO">
                  </div>

                  <div class="form-group">
                    <label for="sellerInputDescription">Объем продажи</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="sellerInputProductValue" v-model="newSeller.value_product">
                    <input v-else type="text" class="form-control" id="sellerInputProductValue" v-model="selectedSeller.value_product" value="selectedSeller.value_product">
                  </div>

                  <div class="form-group">
                    <div class="form-check">
                      <input v-if="formAction === 'Создать'" v-model="newSeller.status_sell" class="form-check-input" type="checkbox" id="ststusCheck">
                      <input v-else v-model="selectedSeller.status_sell" value="selectedSeller.status_sell" class="form-check-input" type="checkbox" id="ststusCheck">
                      <label class="form-check-label" for="ststusCheck">Статус</label>
                    </div>
                  </div>

                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Закрыть</button>
                  <button v-if="formAction === 'Создать'" type="button" class="btn yellow_button" @click.prevent="createSeller()">{{ formAction }}</button>
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
                  <h5 class="modal-title">Просмотр продавца</h5>
                </div>
                <div class="modal-body">
                  <p>Id продавца: <span>{{ selectedSeller.id_sell }}</span></p>
                  <p>Имя: <span>{{ selectedSeller.FIO }}</span></p>
                  <p>Объем продажи: <span>{{ selectedSeller.value_product }}</span></p>
                  <p v-if="selectedSeller.status_sell === true">Статус: <span class="success_text">Работает</span></p>
                  <p v-if="selectedSeller.status_sell === false">Статус: <span class="error_text">Уволен</span></p>
                </div>
                <div class="modal-footer">
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
