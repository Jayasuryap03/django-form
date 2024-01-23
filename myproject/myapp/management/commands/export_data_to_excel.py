# myapp/management/commands/export_data_to_excel.py
import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import UserData

class Command(BaseCommand):
    help = 'Export data to Excel'

    def handle(self, *args, **options):
        # Retrieve data from the database
        queryset = UserData.objects.all()

        # Convert queryset to a DataFrame
        data_frame = pd.DataFrame(list(queryset.values()))

        # Specify the path where you want to save the Excel file
        excel_file_path = 'userdata_export.xlsx'

        # Export the DataFrame to Excel
        data_frame.to_excel(excel_file_path, index=False)

        self.stdout.write(self.style.SUCCESS(f'Data exported to {excel_file_path}'))
