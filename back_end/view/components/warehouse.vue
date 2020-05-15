const Warehouse  = {
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

    getAllClassifiers: function() {
      const url = '/api/classifier/read_all'

      axios.get(url)
        .then(response => {
          console.log(this.classifiers);
          if (Array.isArray(response.data.data)) {
            console.log('array');
            this.classifiers = response.data.data
          } else {
            console.log('object');
            this.classifiers = [response.data.data];
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },

    createWarehouse: function() {
      const url = '/api/warehouse/create';

      this.newWarehouse.receipt_date = `${this.newWarehouse.year}${this.newWarehouse.month}${this.newWarehouse.day}`

      axios.post(url, this.newWarehouse)
        .then(response => {

          console.log(this.newWarehouse)

          console.log(response);

          this.showPostModal = false;
          this.getAllWarehouses();
          this.showActionText('success', 'Warehouse was created');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getAllWarehouses: function() {
      const url = '/api/warehouse/read_all'

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

      const url = `/api/warehouse/read/${id_wh}`;

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

      const url = `/api/warehouse/read/${id_wh}`;

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

      const url = `/api/warehouse/update/${id_wh}`;

      this.selectedWarehouse.receipt_date = `${this.selectedWarehouse.year}${this.selectedWarehouse.month}${this.selectedWarehouse.day}`

      console.log(this.selectedWarehouse)

      axios.put(url, this.selectedWarehouse)
        .then(response => {
          console.log(response);

          this.showPostModal = false;
          this.getAllWarehouses();
          this.showActionText('success', 'Warehouse was updated');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    deleteWarehouseById: function(data) {
      let id_wh = data.target.value;

      const url = `/api/warehouse/delete/${id_wh}`;

      axios.delete(url)
        .then(response => {

          this.getAllWarehouses();
          this.showActionText('success', 'Warehouse was deleted');
        })
        .catch((error) => {
          if (error.response.data.code === 23000) {
            this.showActionText('error', 'Can not Delete Row. Foreign Key Reference Constraint');
          }
        });
    },
  },
  mounted() {
    axios.get(`/api/warehouse/read_all`)
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
          <span>Склады</span>
          <button v-on:click="showPostModal = true; formAction = 'Создать'; getAllClassifiers()" type="button" class="btn yellow_button">Создать</button>
          <button v-on:click="getAllWarehouses" type="button" class="btn purple_button">Обновить</button>
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
            <th>Код классификатора</th>
            <th>Поставщик</th>
            <th>Дата поставки</th>
            <th>Действия</th>
            <!-- <th>Classifier Code</th>
            <th>Supplier</th>
            <th>Receipt Date</th>
            <th>Actions</th> -->
          </tr>
        </thead>

        <tbody>
          <tr v-for="warehouse in warehouses">
            <td>{{ warehouse.code }}</td>
            <td>{{ warehouse.supplier }}</td>
            <td>{{ warehouse.receipt_date }}</td>
            <td>
              <button v-bind:value="warehouse.id_wh" v-on:click="getWarehouseById" type="button" class="btn blue_button">Посмотреть</button>
              <button v-bind:value="warehouse.id_wh" v-on:click="showPostModal = true; formAction = 'Редактировать'; getWarehouseByIdOnlyData($event, warehouse.id_wh)" type="button" class="btn green_button">Редактировать</button>
              <button v-bind:value="warehouse.id_wh" v-on:click="deleteWarehouseById" type="button" class="btn red_button">Удалить</button>
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
                  <h5 class="modal-title">{{ formAction }} склад</h5>
                </div>
                <div class="modal-body">
                  <p v-if="formAction === 'Редактировать'">Id: <span>{{ selectedWarehouse.id_wh }}</span></p>

                  <div v-if="formAction === 'Создать'" class="form-group">
                    <label for="warehouseInputName">Код классификатора</label>
                    <select v-model="newWarehouse.code" class="form-control" id="warehouseInputCode">
                      <option v-for="classifier in classifiers">{{ classifier.code }}</option>
                    </select>
                  </div>
                  <div v-else class="form-group">
                    <p>Код классификатора: <span>{{ selectedWarehouse.code }}</span></p>
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputDescription">Поставщик</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="warehouseInputSupplier" v-model="newWarehouse.supplier">
                    <input v-else type="text" class="form-control" id="warehouseInputSupplier" v-model="selectedWarehouse.supplier" value="selectedWarehouse.supplier">
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputDescription">Дата поставки</label>
                    <!-- <input v-if="formAction === 'Create'" type="text" class="form-control" id="warehouseInputDate" v-model="newWarehouse.receipt_date"> -->
                    <!-- <input v-else type="text" class="form-control" id="warehouseInputDate" v-model="selectedWarehouse.receipt_date" value="selectedWarehouse.receipt_date"> -->

                    <div class="row">
                      <div class="col">
                        <input v-if="formAction === 'Создать'" v-model="newWarehouse.month" type="text" class="form-control" placeholder="Месяц(MM)">
                        <input v-else type="text" v-model="selectedWarehouse.month" value="selectedWarehouse.month" class="form-control" placeholder="Месяц(MM)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Создать'" v-model="newWarehouse.day" type="text" class="form-control" placeholder="День(DD)">
                        <input v-else type="text" v-model="selectedWarehouse.day" value="selectedWarehouse.day" class="form-control" placeholder="День(DD)">
                      </div>
                      <div class="col">
                        <input v-if="formAction === 'Создать'" v-model="newWarehouse.year" type="text" class="form-control" placeholder="Год(YYYY)">
                        <input v-else type="text" v-model="selectedWarehouse.year" value="selectedWarehouse.year" class="form-control" placeholder="Год(YYYY)">
                      </div>
                    </div>
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputDescription">Объем поставки</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="warehouseInputProductValue" v-model="newWarehouse.value_product">
                    <input v-else type="text" class="form-control" id="warehouseInputProductValue" v-model="selectedWarehouse.value_product" value="selectedWarehouse.value_product">
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputPrice">Цена</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="warehouseInputPrice" v-model="newWarehouse.price">
                    <input v-else type="text" class="form-control" id="warehouseInputPrice" v-model="selectedWarehouse.price" value="selectedWarehouse.price">
                  </div>

                  <div class="form-group">
                    <label for="warehouseInputPrice">Изначальное кол-во товара</label>
                    <input v-if="formAction === 'Создать'" type="text" class="form-control" id="warehouseFirstValue" v-model="newWarehouse.first_value">
                    <input v-else type="text" class="form-control" id="warehouseFirstValue" v-model="selectedWarehouse.first_value" value="selectedWarehouse.first_value">
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn red_button" v-on:click="showPostModal = false">Закрыть</button>
                  <button v-if="formAction === 'Создать'" type="button" class="btn yellow_button" @click.prevent="createWarehouse()">{{ formAction }}</button>
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
                  <h5 class="modal-title">Просмотр склада</h5>
                </div>
                <div class="modal-body">
                  <p>Id склада: <span>{{ selectedWarehouse.id_wh }}</span></p>
                  <p>Код классификатора: <span>{{ selectedWarehouse.code }}</span></p>
                  <p>Поставщик: <span>{{ selectedWarehouse.supplier }}</span></p>
                  <p>Дата поставки: <span>{{ selectedWarehouse.receipt_date }}</span></p>
                  <p>Объем поставки: <span>{{ selectedWarehouse.value_product }}</span></p>
                  <p>Цена: <span>{{ selectedWarehouse.price }}</span></p>
                  <p>Изначальное кол-во товара: <span>{{ selectedWarehouse.first_value }}</span></p>
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
