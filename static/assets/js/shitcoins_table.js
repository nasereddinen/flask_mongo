fetch("/static/assets/js/products.json")
.then(function(response){
   return response.json();
})
.then(function(products){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let product of products){
      out += `
         <tr>
            <td>${product.ID}</td>
            <td>${product.Name}</td>
            
         </tr>
      `;
   }
 
   placeholder.innerHTML = out;
});