const Home  = {
  data () {
    return {
      loading: true,
      aggregate_data: {}
    }
  },
  methods: {
    getAllCountData: function() {
      const url = '/count'

      this.loading = true;

      axios.get(url)
        .then(response => {
          response.data.data.forEach(row => {
            this.aggregate_data[row.table_name] = row.row_count;
          })

          console.log(this.aggregate_data)

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  mounted() {
    axios.get(`/count`)
      .then(response => {
          response.data.data.forEach(row => {
            this.aggregate_data[row.table_name] = row.row_count;
          })

          console.log(this.aggregate_data)

          this.loading = false;
        })
        .catch((error) => {
          console.log(error);
        });
  },
  template: `
  <div class="container">
    <div class="header">
      <div class="row">
        <h1>
          <span>Home</span>
          <button v-on:click="getAllCountData" type="button" class="btn purple_button">Reload</button>
        </h1>
      </div>
      <div v-if="loading === false">
        <h2>Total</h2>
        <p>Classifiers: <span class="cherry_color">{{ aggregate_data.classifier }}</span></p>
        <p>Producs: <span class="cherry_color">{{ aggregate_data.product }}</span></p>
        <p>Sellers: <span class="cherry_color">{{ aggregate_data.seller }}</span></p>
        <p>Suppliers: <span class="cherry_color">{{ aggregate_data.supplier }}</span></p>
        <p>Warehouses: <span class="cherry_color">{{ aggregate_data.warehouse }}</span></p>
      </div>
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
