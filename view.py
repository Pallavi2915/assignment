import csv
from django.shortcuts import render
from forms import CSVUploadForm
from models import Transaction

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
            
            rows_saved = 0
            for i, row in enumerate(csv_data):
                if i >= 60:
                    break
                
                # Save only the required columns
                invoice_id = row[0]
                product_line = row[1]
                unit_price = row[2]
                quantity = row[3]
                tax = row[4]
                total = row[5]
                date = row[6]
                time = row[7]
                
                # Create a Transaction object and save it
                transaction = Transaction(
                    invoice_id=invoice_id,
                    product_line=product_line,
                    unit_price=unit_price,
                    quantity=quantity,
                    tax=tax,
                    total=total,
                    date=date,
                    time=time
                )
                transaction.save()
                rows_saved += 1
            
            return render(request, 'transactions/success.html', {'rows_saved': rows_saved})
    else:
        form = CSVUploadForm()
    
    return render(request, 'transactions/upload.html', {'form': form})

def transactions_health_beauty(request):
    transactions = Transaction.objects.filter(product_line='Health and beauty')
    return render(request, 'transactions/health_beauty.html', {'transactions': transactions})
